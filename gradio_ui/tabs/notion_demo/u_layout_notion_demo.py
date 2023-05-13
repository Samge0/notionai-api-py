#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-03-28 14:40
# describe：
import gradio as gr

from gradio_ui.g_utils.common import u_common_layout
from gradio_ui.tabs.notion_demo import u_handler_notion_demo
from utils.u_config import g_config


def create_layout():
    """ 构建布局 """
    with gr.Row().style(equal_height=True):
        with gr.Column(scale=1):
            api_url = gr.Textbox(show_label=True, label="代理Url", placeholder="请输入自定义的代理请求地址（如果是部署在国外服务器，可空）", lines=1, max_lines=1, value=g_config.api_url)
            with gr.Row().style(equal_height=True):
                notion_token = gr.Textbox(show_label=True, label="Notion_token_v2", placeholder="请输入Notion的token_v2值", lines=1, max_lines=1, value=g_config.notion_token)
                space_id = gr.Textbox(show_label=True, label="space_id", placeholder="请输入Notion的space_id值", lines=1, max_lines=1, value=g_config.space_id)
            with gr.Row().style(equal_height=True):
                topic = u_common_layout.get_topic_layout()
                prompt_type = u_common_layout.get_prompt_type_layout()
            with gr.Row().style(equal_height=True):
                tone = u_common_layout.get_tone_layout()
                translate = u_common_layout.get_translate_layout()
            prompt = gr.Textbox(show_label=True, label="提示内容（prompt）", placeholder="请输入提示内容（prompt）,与topic非相关强相关", lines=3, max_lines=3)
            context = gr.Textbox(show_label=True, label="上下文内容（context）", placeholder="请输入上下文内容（context）,与prompt_type、tone、translate强相关，与topic非相关", lines=6, max_lines=6)
            with gr.Row().style(equal_height=True):
                button_load = gr.Button("加载缓存")
                button = gr.Button("生成内容")
        with gr.Column(scale=1):
            result = gr.Textbox(
                label="生成结果",
                placeholder="这里展示生成结果",
                lines=20,
                max_lines=20
            )
            result_api_info = gr.Textbox(
                label="API请求参考",
                placeholder="这里展示API请求的参考信息",
                lines=10,
                max_lines=10
            )
    button.click(u_handler_notion_demo.handler, inputs=[topic, prompt_type, tone, translate, prompt, context, notion_token, space_id, api_url], outputs=[result, result_api_info])
    button_load.click(u_handler_notion_demo.load, inputs=[], outputs=[topic, prompt_type, tone, translate, prompt, context, notion_token, space_id, api_url])
