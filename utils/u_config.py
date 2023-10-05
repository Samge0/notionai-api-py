#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-04-28 23:33
# describe：
import os
from typing import Optional

from models.m_notion import NotionRequestBase
from utils import u_file, u_json


class GlobalConfig(NotionRequestBase):
    """ 全局配置模型 """
    access_token: Optional[str] = ""


# 配置文件路径 - 可能不存在
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_config_json_path = f"{project_dir}/config.json"
# 配置字典 - 可能空字典
_config_dict = u_json.eval_dict(u_file.read(_config_json_path))

# 全局配置对象 - 环境变量的值最高
g_config = GlobalConfig.parse_obj(_config_dict) if isinstance(_config_dict, dict) else GlobalConfig()

# 读取环境变量的值 - 如果存在的话
g_config.model = os.environ.get('NOTION_MODEL') or g_config.model
g_config.access_token = os.environ.get('ACCESS_TOKEN') or g_config.access_token
g_config.prompt_type = os.environ.get('NOTION_PROMPT_TYPE') or g_config.prompt_type
g_config.tone = os.environ.get('NOTION_TONE') or g_config.tone
g_config.topic = os.environ.get('NOTION_TOPIC') or g_config.topic
g_config.translate = os.environ.get('NOTION_TRANSLATE') or g_config.translate
g_config.notion_token = os.environ.get('NOTION_TOKEN') or g_config.notion_token
g_config.space_id = os.environ.get('NOTION_SPACE_ID') or g_config.space_id
g_config.api_url = os.environ.get('NOTION_API_URL') or g_config.api_url


def merge_request(request: NotionRequestBase):
    """ 将 请求体的值 与 g_config的值 合并返回，优先使用 request的值 """
    request.model = request.model or g_config.model
    request.prompt_type = request.prompt_type or g_config.prompt_type
    request.tone = request.tone or g_config.tone
    request.topic = request.topic or g_config.topic
    request.translate = request.translate or g_config.translate
    request.notion_token = request.notion_token or g_config.notion_token
    request.space_id = request.space_id or g_config.space_id
    request.api_url = request.api_url or g_config.api_url


def get_prompt_type(request: NotionRequestBase):
    """ 获取 提示类型 """
    return request.prompt_type or g_config.prompt_type


def get_tone(request: NotionRequestBase):
    """ 获取 语调类型 """
    return request.tone or g_config.tone


def get_topic(request: NotionRequestBase):
    """ 获取 主题 """
    return request.topic or g_config.topic


def get_translate(request: NotionRequestBase):
    """ 获取 翻译语言 """
    return request.translate or g_config.translate


def get_notion_token(request: NotionRequestBase):
    """ 获取 Notion的token_v2 """
    return request.notion_token or g_config.notion_token


def get_space_id(request: NotionRequestBase):
    """ 获取 Notion的space_id """
    return request.space_id or g_config.space_id


def get_api_url(request: NotionRequestBase):
    """ 获取 代理的api主机地址 """
    return request.api_url or g_config.api_url
