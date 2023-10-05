#!/usr/bin/ruby
# -*- coding : utf-8 -*-
# author：samge
# data：2023-02-28 15:11
# describe：
from typing import Optional

from pydantic import BaseModel

# 默认的api请求地址
DEFAULT_API_URL = "https://www.notion.so"


class NotionRequestBase(BaseModel):
    """notion基础请求体"""
    model: Optional[str] = None  # 模型，例如 openai-3 、 openai-4
    prompt_type: Optional[str] = None  # 提示类型：helpMeWrite=帮助我写作, continueWriting=继续写作, changeTone=改变语气, summarize=总结, improveWriting=改善写作, fixSpellingGrammar=纠正拼写和语法错误, translate=翻译, explainThis=解释这个, makeLonger=延长篇幅, makeShorter=缩短篇幅, findActionItems=找到行动项, simplifyLanguage=简化语言, helpMeEdit=帮助我编辑
    tone: Optional[str] = None  # 语调类型：professional=专业的, casual=随便的，非正式的, straightforward=直截了当的，简单易懂的, confident=自信的, friendly=友好的
    topic: Optional[str] = None  # 主题：brainstormIdeas=头脑风暴想法, blogPost=博客文章, outline=大纲, socialMediaPost=社交媒体帖子, pressRelease=新闻稿, creativeStory=创意故事, essay=论文, poem=诗, meetingAgenda=会议议程, prosConsList=优点清单, jobDescription=工作描述, salesEmail=销售电子邮件, recruitingEmail=招聘电子邮件
    translate: Optional[str] = None  # 翻译语言：english=英语, korean=汉语, chinese=中文, japanese=日语, spanish=西班牙语, russian=俄语, french=法语, german=德语, italian=意大利语, portuguese=葡萄牙语, dutch=荷兰语, indonesia=印度尼西亚语, tagalog=塔加路语（菲律宾语）, vietnamese=越南语
    notion_token: Optional[str] = None  # Notion的token_v2
    space_id: Optional[str] = None  # Notion的space_id
    api_url: Optional[str] = None  # 代理的api主机地址


class NotionRequest(NotionRequestBase):
    """notion请求体"""
    prompt: Optional[str] = None  # 提示内容（文本）【可选，但prompt与context不能同时为空】
    context: Optional[str] = None  # 上下文内容（文本）【可选，但prompt与context不能同时为空。部分类型必选：help_me_write、help_me_edit、translate、change_tone，如果为空则取prompt】


