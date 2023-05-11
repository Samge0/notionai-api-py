#!/usr/bin/ruby
# -*- coding : utf-8 -*-
# author：samge
# data：2023-05-10 20:56
# describe：

from fastapi import Depends, FastAPI, Header

from models.m_notion import NotionRequest
from utils import u_http, u_config, u_api_handler
from utils.u_config import g_config


async def verify_token(Authorization: str = Header(...)):
    """ token简易验证 """
    if Authorization != f"Bearer {g_config.access_token}":
        print(f"认证失败：{Authorization}")
        u_http.fail403(msg='Authorization header invalid')


app = FastAPI(dependencies=[Depends(verify_token)])


@app.post("/ai/notion")
async def ai_notion(request: NotionRequest):
    # 整合请求参数
    u_config.merge_request(request)

    # 检查参数
    check_statis, msg = u_api_handler.check_parameters(request)
    if not check_statis:
        return u_http.fail400(msg=msg)

    # 请求结果
    status, result = u_api_handler.get_notion_result(request)
    if not status:
        return u_http.fail400(msg=result)

    return u_http.success(result)
