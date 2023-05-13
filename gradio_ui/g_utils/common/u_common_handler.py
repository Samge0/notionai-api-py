#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-03-28 14:47
# describe：
import math


def check_url(url, check_empty: bool = True) -> (bool, str):
    """
    检查链接是否符合要求
    :param url:
    :param check_empty:
    :return:
    """
    if check_empty and not url:
        return False, "【URL】不能为空"
    if url and not url.startswith('http'):
        return False, "【URL】需要以http开头"
    return True, None