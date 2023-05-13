#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-03-24 17:50
# describe：
import gradio as gr

from gradio_ui.tabs.notion_demo import u_layout_notion_demo

"""
gradio界面
参考：https://blog.csdn.net/LuohenYJ/article/details/127489768
官方文档：https://github.com/gradio-app/gradio
"""


with gr.Blocks() as app:
    gr.Markdown("## NotionAI 辅助工具")
    with gr.Tab("Api-Demo"):
        u_layout_notion_demo.create_layout()


app.launch(share=False, inbrowser=False, debug=True, server_name="0.0.0.0", server_port=7861)
