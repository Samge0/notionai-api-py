#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-05-12 0:30
# describe：
from models.m_notion import NotionRequest
from utils.notionai.enums import TopicEnum, PromptTypeEnum, TranslateLanguageEnum, ToneEnum
from utils.notionai.notionai import NotionAI


def check_parameters(request: NotionRequest) -> (bool, str):
    """
    检查参数
    :param request:
    :return:
    """

    if not request.prompt and not request.context:
        return False, "参数[prompt、context]不能同时为空"

    notion_token = request.notion_token
    if not notion_token:
        return False, "参数[notion_token]不能为空"

    space_id = request.space_id
    if not space_id:
        return False, "参数[space_id]不能为空"

    topic = request.topic
    if topic and topic not in [e.value for e in TopicEnum]:
        return False, "参数[topic]不在支持范围"

    prompt_type = request.prompt_type
    if prompt_type and prompt_type not in [e.value for e in PromptTypeEnum]:
        return False, "参数[prompt_type]不在支持范围"

    translate = request.translate
    if translate and translate not in [e.value for e in TranslateLanguageEnum]:
        return False, "参数[translate]不在支持范围"

    tone = request.tone
    if tone and tone not in [e.value for e in ToneEnum]:
        return False, "参数[tone]不在支持范围"

    if not topic and not prompt_type and not translate and not tone:
        return False, "参数[topic、prompt_type、translate、tone]不能同时为空"

    return True, None


def get_notion_result(request: NotionRequest) -> (bool, str):
    """
    获取请求结果
    :param request:
    :return:
    """
    context = request.context or request.prompt
    notion_ai = NotionAI(request.notion_token, request.space_id, api_url=request.api_url)
    if request.topic:
        # 根据提示进行主题书写（只需要提示prompt，不需要上下文内容context），可选参数
        result = notion_ai.writing_with_topic(topic=TopicEnum(request.topic), prompt=request.prompt)
    elif request.prompt_type:
        # 根据上下文内容+提示生成内容
        result = hande_prompt_type(request, notion_ai)
    elif request.tone:
        # 根据文本进行语调调整（需要上下文内容context）
        result = notion_ai.change_tone(tone=ToneEnum(request.tone), context=context)
    elif request.translate:
        # 根据文本进行翻译（需要上下文内容context）
        result = notion_ai.translate(language=TranslateLanguageEnum(request.translate), context=context)
    else:
        return False, "未命中的请求类型"
    return True, result


def hande_prompt_type(request: NotionRequest, notion_ai: NotionAI):
    """
    处理 prompt_type 的请求
        其中help_me_write、help_me_edit、translate、change_tone这几个类型的context是需要取值的，如果context为空，则取prompt的值
    :param request:
    :param notion_ai:
    :return:
    """
    context = request.context or request.prompt
    if request.prompt_type == PromptTypeEnum.help_me_write:
        result = notion_ai.help_me_write(prompt=request.prompt, context=context, page_title="")
    elif request.prompt_type == PromptTypeEnum.help_me_edit:
        result = notion_ai.help_me_edit(prompt=request.prompt, context=context)
    elif request.prompt_type == PromptTypeEnum.translate:
        result = notion_ai.translate(language=TranslateLanguageEnum(request.translate), context=context)
    elif request.prompt_type == PromptTypeEnum.change_tone:
        result = notion_ai.change_tone(tone=ToneEnum(request.tone), context=context)
    else:
        result = notion_ai.writing_with_prompt(prompt_type=PromptTypeEnum(request.prompt_type), context=context, page_title="")
    return result
