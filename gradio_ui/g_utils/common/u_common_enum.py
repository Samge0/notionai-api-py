#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-03-31 10:35
# describe：
from utils.notionai.enums import ExtendedEnum


class TopicEnumWithDoc(ExtendedEnum):
    """ 主题枚举 - 中文映射方便ui展示"""
    brainstormIdeas = "头脑风暴想法"
    blogPost = "博客文章"
    outline = "大纲"
    socialMediaPost = "社交媒体帖子"
    pressRelease = "新闻稿"
    creativeStory = "创意故事"
    essay = "论文"
    poem = "诗"
    meetingAgenda = "会议议程"
    prosConsList = "优点清单"
    jobDescription = "工作描述"
    salesEmail = "销售电子邮件"
    recruitingEmail = "招聘电子邮件"


class TranslateLanguageEnumWithDoc(ExtendedEnum):
    """ 翻译枚举 - 中文映射方便ui展示 """
    english = "英语"
    korean = "韩语"
    chinese = "中文"
    japanese = "日语"
    spanish = "西班牙语"
    russian = "俄语"
    french = "法语"
    german = "德语"
    italian = "意大利语"
    portuguese = "葡萄牙语"
    dutch = "荷兰语"
    indonesian = "印度尼西亚语"
    tagalog = "塔加路语（菲律宾语）"
    vietnamese = "越南语"


class PromptTypeEnumWithDoc(ExtendedEnum):
    """ 提示类型枚举 - 中文映射方便ui展示 """
    helpMeWrite = "帮助我写作"
    continueWriting = "继续写作"
    changeTone = "改变语气"
    summarize = "总结"
    improveWriting = "改善写作"
    fixSpellingGrammar = "纠正拼写和语法错误"
    translate = "翻译"
    explainThis = "解释这个"
    makeLonger = "延长篇幅"
    makeShorter = "缩短篇幅"
    findActionItems = "找到行动项"
    simplifyLanguage = "简化语言"
    helpMeEdit = "帮助我编辑"


class ToneEnumWithDoc(ExtendedEnum):
    """ 语调枚举 - 中文映射方便ui展示 """
    professional = "专业的"
    casual = "随便的，非正式的"
    straightforward = "直截了当的，简单易懂的"
    confident = "自信的"
    friendly = "友好的"


def get_enum_name_by_value(enum_class, value) -> str:
    """
    根据枚举的value值取name
    :param enum_class:
    :param value:
    :return:
    """
    for enum_member in enum_class:
        if enum_member.value == value:
            return enum_member.name
    return ""


def get_enum_value_by_name(enum_class, name) -> str:
    """
    根据枚举的name值取value
    :param enum_class:
    :param name:
    :return:
    """
    for enum_member in enum_class:
        if enum_member.name == name:
            return enum_member.value
    return ""
