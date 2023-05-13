#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-03-28 14:47
# describe：

import gradio as gr

from gradio_ui.g_utils.common.u_common_enum import TopicEnumWithDoc, TranslateLanguageEnumWithDoc, \
    PromptTypeEnumWithDoc, ToneEnumWithDoc


def get_topic_layout():
    """
    获取 主题 下拉选择框
    :return:
    """
    return get_enum_layout(TopicEnumWithDoc, "请选择主题（topic）：")


def get_translate_layout():
    """
    获取 翻译 下拉选择框
    :return:
    """
    return get_enum_layout(TranslateLanguageEnumWithDoc, "请选择翻译语言（translate）：")


def get_prompt_type_layout():
    """
    获取 提示类型 下拉选择框
    :return:
    """
    return get_enum_layout(PromptTypeEnumWithDoc, "请选择提示类型（prompt_type）：")


def get_tone_layout():
    """
    获取 语调 下拉选择框
    :return:
    """
    return get_enum_layout(ToneEnumWithDoc, "请选择语调（tone）：")


def get_enum_layout(_enum, label: str, value: str = ""):
    """
    获取 某个枚举的 下拉选择框
    :return:
    """
    return gr.components.Dropdown(
        choices=[member.value for member in _enum],
        value=value,
        label=label
    )
