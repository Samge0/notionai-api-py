#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-03-20 11:32
# describe：


"""
字典相关操作工具类，主要可用符号.链式读取字典中的值
"""
from scrapy_core.utils import u_re


def get_dict_value(_dict: dict, key: str):
    """
    获取字典的值，适配了多层级数据读取
    :param _dict: 字典对象
    :param key: 需要提取的key，如果有多层级请用.连接，例如：data.html.text
    :return:
    """
    if not _dict or not key or not isinstance(_dict, dict):
        return None
    if '.' not in key:
        return _dict.get(key) or ''
    try:
        for k in key.split('.'):
            # 判断是否包含 [数字] 这样的格式
            index_value = u_re.search_one_lr(k, left_str='\[', right_str='\]') or ''
            if len(index_value) > 0:
                k = k.split('[')[0]
                _dict = get_dict_lst_with_index(_dict, k, int(index_value))
            else:
                _dict = _dict.get(k) if _dict else None
        return _dict
    except Exception as e:
        print(f"get_dict_value(_dict, '{key}')异常：{e}")
        return None


def get_dict_lst_first(_dict: dict, key: str):
    """
    获取字典中某个列表的首个值

    :param _dict: 字典对象
    :param key: 需要提取的key，如果有多层级请用.连接，例如：data.html.text
    :return:
    """
    return get_dict_lst_with_index(_dict, key, 0)


def get_dict_lst_with_index(_dict: dict, key: str, index: int):
    """
    获取字典中某个列表的首个值

    :param _dict: 字典对象
    :param key: 需要提取的key，如果有多层级请用.连接，例如：data.html.text
    :param index: 列表下标的索引值
    :return:
    """
    if not _dict or index < 0:
        return None
    lst = get_dict_value(_dict, key) or []
    lst_size = len(lst)
    if lst_size <= 0:
        return None
    return lst[index] if index < lst_size else None
