#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 下午7:25
# @Author  : Samge
import hashlib


"""
内置的md5生成工具类
"""


def create_md5(v: str, with_csharp: bool = False) -> str:
    """
    生成32位长度的md5
    :param v:
    :param with_csharp: 是否兼容c#项目那边的md5
    :return:
    """
    if not with_csharp:
        return hashlib.md5(v.encode('utf-8')).hexdigest() if v else None
    try:
        return hashlib.md5(v.encode('GBK')).hexdigest() if v else None
    except Exception as e:
        return hashlib.md5(v.encode('utf-8')).hexdigest() if v else None


if __name__ == '__main__':
    print(create_md5("test"))
