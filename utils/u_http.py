#!/usr/bin/ruby
# -*- coding : utf-8 -*-
# author：samge
# data：2023-02-28 14:56
# describe：


def common_response(code, data, msg) -> dict:
    """
    统一回复格式
    :param code: 响应码
    :param data: 数据
    :param msg: 提示消息
    :return:
    """
    return {
        'code': code,
        'data': data,
        'msg': msg,
    }


def success(data) -> dict:
    """
    成功的响应
    :param data: 数据
    :return:
    """
    return common_response(200, data, 'success')


def fail400(msg: str = '参数错误') -> dict:
    """ 失败的响应 """
    return common_response(400, None, msg)


def fail403(msg: str = '权限校验失败') -> dict:
    """ 权限校验失败 """
    return common_response(403, None, msg)


def fail500(msg: str = '服务异常，请稍后重') -> dict:
    """ 服务错误 """
    return common_response(500, None, msg)
