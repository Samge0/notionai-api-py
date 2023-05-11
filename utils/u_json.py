#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 下午4:45
# @Author  : Samge


"""
“安全”的json字符转字典对象的工具类，该“安全”由try except冠名赞助……
"""


null, false, true = None, False, True


def eval_dict(v: str, default_value: dict = {}) -> dict:
    """
    这里统一处理eval对 null, false, true 这几个值得解析
    :param v:
    :param default_value:
    :return:
    """
    try:
        return eval(v)
    except Exception as e:
        return default_value
