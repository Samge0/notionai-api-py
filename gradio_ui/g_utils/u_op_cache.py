#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-03-28 11:38
# describe：
import json
import os

from utils import u_json, u_file

"""
操作相关的缓存工具
"""


cache_dir = 'gradio_cache/operation_cache'


def __init_cache_dir():
    """ 初始化缓存目录 """
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)


def save_cache(key: str, value):
    """
    保存一般缓存数据
    :param key:
    :param value:
    :return:
    """
    path = __get_common_cache_path()
    current_cache_dict = u_json.eval_dict(u_file.read(path))
    current_cache_dict[key] = value
    txt = json.dumps(current_cache_dict, ensure_ascii=False, indent=4).encode('utf-8')
    txt = str(txt, encoding='utf-8')
    u_file.save(txt, path)
    print(f"【{key}】缓存保存在：{path}")


def read_cache(key: str, default_value):
    """
    读取一般缓存数据
    :param key:
    :param default_value:
    :return:
    """
    path = __get_common_cache_path()
    current_cache_dict = u_json.eval_dict(u_file.read(path))
    return current_cache_dict.get(key) or default_value


def __get_common_cache_path() -> str:
    """
    获取一般缓存文件路径
    :return:
    """
    __init_cache_dir()
    return f'{cache_dir}/common_cache.json'


def __get_url(request, is_dtl: bool) -> str:
    return request.url_dtl if is_dtl else request.url_lst
