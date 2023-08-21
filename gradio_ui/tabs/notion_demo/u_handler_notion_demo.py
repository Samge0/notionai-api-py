#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-03-28 14:43
# describe：
import codecs
import json

from gradio_ui.g_utils import u_op_cache
from gradio_ui.g_utils.common import u_common_enum
from models.m_notion import NotionRequest
from utils import u_api_handler, u_config
from gradio_ui.g_utils.common.u_common_enum import TopicEnumWithDoc, TranslateLanguageEnumWithDoc, \
    PromptTypeEnumWithDoc, ToneEnumWithDoc
from utils.u_config import g_config

CACHE_KEY = "NotionAI_Api_Parameters_Cache"


def load():
    """ 加载缓存 """
    cache_dict = u_op_cache.read_cache(CACHE_KEY, {})
    request = NotionRequest.parse_obj(cache_dict) if isinstance(cache_dict, dict) else NotionRequest()
    return [
        u_common_enum.get_enum_value_by_name(TopicEnumWithDoc, request.topic),
        u_common_enum.get_enum_value_by_name(PromptTypeEnumWithDoc, request.prompt_type),
        u_common_enum.get_enum_value_by_name(ToneEnumWithDoc, request.tone),
        u_common_enum.get_enum_value_by_name(TranslateLanguageEnumWithDoc, request.translate),
        request.prompt,
        request.context,
        request.notion_token or g_config.notion_token,
        request.space_id or g_config.space_id,
        request.api_url or g_config.api_url
    ]


def get_result_api_info(request):
    """
    api请求参考信息
    :param request:
    :return:
    """
    return f"""请求地址：http://192.168.5.116:18233/ai/notion
请求方法：POST
请求头：
Content-Type: application/json
Authorization: Bearer {g_config.access_token}
请求体（JSON）：
{json.dumps(request.dict(), ensure_ascii=False)}
"""


def handler(topic, prompt_type, tone, translate, prompt, context, notion_token, space_id, api_url):
    """
    统计信息
    :return:
    """
    request = NotionRequest(
        topic=u_common_enum.get_enum_name_by_value(TopicEnumWithDoc, topic),
        prompt_type=u_common_enum.get_enum_name_by_value(PromptTypeEnumWithDoc, prompt_type),
        tone=u_common_enum.get_enum_name_by_value(ToneEnumWithDoc, tone),
        translate=u_common_enum.get_enum_name_by_value(TranslateLanguageEnumWithDoc, translate),
        prompt=prompt,
        context=context,
        notion_token=notion_token,
        space_id=space_id,
        api_url=api_url,
    )

    # 合并参数
    u_config.merge_request(request)

    # 检查参数
    check_statis, msg = u_api_handler.check_parameters(request)
    if not check_statis:
        return [f"【操作失败】：{msg}", ""]

    # 缓存数据
    u_op_cache.save_cache(CACHE_KEY, request.__dict__)

    # api请求参考信息
    result_api_info = get_result_api_info(request)

    # 请求结果
    status, result = u_api_handler.get_notion_result(request)
    return [result, result_api_info]


def unicode_to_chinese(unicode_str):
    """
    unicode编码内容转为明文中文
    :param unicode_str:
    :return:
    """
    chinese_str = codecs.decode(unicode_str, 'unicode_escape')
    return chinese_str
