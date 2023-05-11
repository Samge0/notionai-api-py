#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-04-28 23:59
# describe：
import os

from utils import u_file

# 缓存目录名称
cache_dir_name = '.cache'


def _get_project_dir() -> str:
    """ 获取项目目录 """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_cache_dir() -> str:
    """ 初始化缓存目录 """
    cache_dir = f"{_get_project_dir()}/{cache_dir_name}"
    u_file.makedirs(cache_dir)
    return cache_dir


def save(filename: str, txt: str) -> str:
    """
    保存缓存
    :param filename: 缓存文件名
    :param txt: 缓存文本内容
    :return: 保存成功 =》 返回缓存文件路径，
             保存失败 =》 None
    """
    file_path = f"{get_cache_dir()}/{filename}"
    return file_path if u_file.save(txt, file_path) else None


def get(filename: str, default_value: str) -> str:
    """
    保存缓存
    :param filename: 缓存文件名
    :param default_value: 取值失败的默认值
    :return:
    """
    file_path = f"{get_cache_dir()}/{filename}"
    return u_file.read(file_path) or default_value
