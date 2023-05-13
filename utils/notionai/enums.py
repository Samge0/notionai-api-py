#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-05-10 23:59
# describe：
from enum import Enum


class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def list_name(cls):
        return list(map(lambda c: c.name, cls))


class TopicEnum(ExtendedEnum):
    """ 主题枚举 """
    brainstorm_ideas = "brainstormIdeas"  # 头脑风暴想法
    blog_post = "blogPost"  # 博客文章
    outline = "outline"  # 大纲
    social_media_post = "socialMediaPost"  # 社交媒体帖子
    press_release = "pressRelease"  # 新闻稿
    creative_story = "creativeStory"  # 创意故事
    essay = "essay"  # 论文
    poem = "poem"  # 诗
    meeting_agenda = "meetingAgenda"  # 会议议程
    pros_cons_list = "prosConsList"  # 优点清单
    job_description = "jobDescription"  # 工作描述
    sales_email = "salesEmail"  # 销售电子邮件
    recruiting_email = "recruitingEmail"  # 招聘电子邮件


class TranslateLanguageEnum(ExtendedEnum):
    """ 翻译枚举 """
    english = "english"  # 英语
    korean = "korean"  # 韩语
    chinese = "chinese"  # 中文
    japanese = "japanese"  # 日语
    spanish = "spanish"  # 西班牙语
    russiab = "russian"  # 俄语
    french = "french"  # 法语
    german = "german"  # 德语
    italian = "italian"  # 意大利语
    portuguese = "portuguese"  # 葡萄牙语
    dutch = "dutch"  # 荷兰语
    indonesia = "indonesia"  # 印度尼西亚语
    tagalog = "tagalog"  # 塔加路语（菲律宾语）
    vietnamese = "vietnamese"  # 越南语


class PromptTypeEnum(ExtendedEnum):
    """ 提示类型枚举 """
    help_me_write = "helpMeWrite"  # 帮助我写作
    continue_writing = "continueWriting"  # 继续写作
    change_tone = "changeTone"  # 改变语气
    summarize = "summarize"  # 总结
    improve_writing = "improveWriting"  # 改善写作
    fix_spelling_grammar = "fixSpellingGrammar"  # 纠正拼写和语法错误
    translate = "translate"  # 翻译
    explain_this = "explainThis"  # 解释这个
    make_longer = "makeLonger"  # 延长篇幅
    make_shorter = "makeShorter"  # 缩短篇幅
    find_action_items = "findActionItems"  # 找到行动项
    simplify_language = "simplifyLanguage"  # 简化语言
    help_me_edit = "helpMeEdit"  # 帮助我编辑


class ToneEnum(ExtendedEnum):
    """ 语调枚举 """
    professional = "professional"  # 专业的
    casual = "casual"  # 随便的，非正式的
    straight_forward = "straightforward"  # 直截了当的，简单易懂的
    confident = "confident"  # 自信的
    friendly = "friendly"  # 友好的
