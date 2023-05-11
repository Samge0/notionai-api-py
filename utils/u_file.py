#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/20 下午5:35
# @Author  : Samge
import base64
import os


"""
文件操作相关工具类，主要有文件读写、base64保存为文件、文件size、文件删除等操作
"""


def save_base64(_base64: str, _path: str) -> bool:
    """保存base64到文件"""
    try:
        if exists(_path):
            return True
        filedata = base64.b64decode(_base64.replace('\n', ''))
        with open(_path, "wb") as fh:
            fh.write(filedata)
            fh.close()
        return True
    except Exception as e:
        print(f'保存base64到文件错误：{e}')
        return False


def save(_txt: str, _path: str, _type: str = 'w+') -> bool:
    """保存文件"""
    try:
        with open(_path, _type, encoding='utf-8') as f:
            f.write(_txt)
            f.flush()
            f.close()
        return True
    except:
        return False


def read(_path: str) -> str:
    """读取文件"""
    result = read_bytes(_path)
    return str(result, encoding='utf-8') if result else ""


def read_bytes(_path: str) -> bytes:
    """读取文件bytes信息"""
    try:
        if is_egg_path(_path):
            return read_file_with_egg(_path)
        if not exists(_path):
            return None
        with open(_path, "rb") as f:
            result = f.read()
            # replace一下，避免使用rb方式读取时，\n变为了\r\n
            result = result.replace(b'\r\n', b'\n') if result else result
            f.close()
            return result
    except:
        return None


def size(file_path) -> float:
    """读取文件大小，单位：M"""
    if not exists(file_path):
        return 0
    return os.path.getsize(file_path) / 1024 / 1024


def remove(file_path: str):
    """删除文件"""
    try:
        os.remove(file_path)
    except:
        pass


def exists(_path: str) -> bool:
    """
    判断是否存在
    :param _path:
    :return:
    """
    return _path and os.path.exists(_path)


def makedirs(_path: str):
    """
    创建多层目录
    :param _path:
    :return:
    """
    if not exists(_path):
        os.makedirs(_path)
        

def read_txt_with_egg(_path: str):
    """
    从egg文件路径中读取文本
    :param _path:
    :return:
    """
    result = read_file_with_egg(_path)
    return str(result, encoding='utf-8') if result else ""


def read_file_with_egg(_path: str):
    """
    从egg文件路径中读取实际的文件信息
    :param _path: 包含egg信息的文件路径
    :return:
    """
    try:

        # 统一格式化路径的斜杆
        _path = (_path or '').replace(os.sep, '/')

        # 如果文件路径存在，则直接读取返回
        if exists(_path):
            return read_bytes(_path)

        # 如果文件路径不符合要求，返回None
        if not is_egg_path(_path):
            print(f"这不是一个.egg相关的路径（{_path}）")
            return None

        # 拆分文件路径，获取egg文件路径，已经egg中需要读取的实际文件路径
        _split = _path.split('.egg/')
        egg_file_path = f"{_split[0]}.egg"
        real_file_path = _split[1]

        # 如果egg文件不存在，返回None
        if not exists(egg_file_path):
            print(f"egg路径（{egg_file_path}）不存在")
            return None

        # 只有在egg路径是文件格式，才使用zipfile进行读取，否则返回None
        if os.path.isfile(egg_file_path):
            import zipfile
            egg_file = zipfile.ZipFile(egg_file_path, 'r')
            namelist = egg_file.namelist() or []
            if real_file_path not in namelist:
                # 如果需要读取的文件路径不再egg中，返回None
                print(f"指定文件路径（{real_file_path}）在egg（{egg_file_path}）中不存在，namelist={namelist}")
                return None
            return egg_file.read(real_file_path)
        else:
            return None

    except Exception as e:
        print(f"读取egg指定文件路径（{_path}）失败：{str(e)}")
        return None


def is_egg_path(_path: str) -> bool:
    """
    是否egg相关的文件路径，
        目前仅判断文件路径中是否有 .egg 字样，并不是特别严谨，但对于目前的scrapyd文件读取够用了
    :param _path:
    :return:
    """
    return _path and '.egg' in _path


def get_goal_dir(goal_dir_name, dir_path: str = os.path.abspath(__file__)):
    """
    从一个目录字符串中截取目标目录的绝对路径
    :param goal_dir_name: 目标目录名
    :param dir_path: 指定的目录地址，默认为当前执行文件的目录地址
    :return:
    """
    if not goal_dir_name or goal_dir_name not in dir_path:
        return None
    _index = dir_path.index(goal_dir_name)
    return f"{dir_path[:_index+len(goal_dir_name)]}"
