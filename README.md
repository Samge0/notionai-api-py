## NotionAI api
一个简易的页面 NotionAI api接口 + 简易的token校验。<br>
本项目使用了[notionai-py项目](https://github.com/Vaayne/notionai-py)，感谢`notionai-py`作者的开源。


### 使用说明
- 复制`config-dev.json`文件为`config.json`并填写自定义的`access_token`；
- 配置`http-client.env.json`后在`test_main.http`中进行接口调试，其中`access_token`的值跟config.json中的一致；

### docker方式运行

[点击这里查看docker说明](docker/README.md)


### 本地源码运行

- 安装依赖
```shell
pip install -r requirements.txt
```

- 运行
```shell
uvicorn run main:app --reload --host 0.0.0.0 --port 8000
```


### 参数说明
【注意】：参数 `topic`、`prompt_type`、`translate`、`tone` 不能同时为空

- [系统配置的参数说明](config-dev.json)
```text
{
  "model": "openai-4",  // 模型，例如 openai-3 、 openai-4
  "access_token": "",  // 自定义的api请求token，可选参数
  "prompt_type": "",  // 根据文本进行上下文连写（需要提示prompt + 上下文内容context），可选参数
  "tone": "",  // 根据文本进行语调调整（需要上下文内容context），可选参数
  "topic": "",  // 根据提示进行主题书写（只需要提示prompt，不需要上下文内容context），可选参数
  "translate": "",  // 根据文本进行翻译（需要上下文内容context），可选参数
  "notion_token": "",  // notion的 token_v2值，可选参数
  "space_id": "",  // notion的 space_id值，可选参数
  "api_url": ""  // 代理的api url，可选参数
}
```


- api请求的参数（`api的参数`比`系统配置的参数`优先级高，方便调用者动态修改）,api的具体调用请参考[test_main.http](test_main.http)
```text
{
  "model": "openai-4",  // 模型，例如 openai-3 、 openai-4
  "prompt": "",  // 提示内容（文本）【可选，但prompt与context不能同时为空】
  "context": "",  // 上下文内容（文本）【可选，但prompt与context不能同时为空。部分类型必选：help_me_write、help_me_edit、translate、change_tone，如果为空则取prompt】
  "prompt_type": "",  // 根据文本进行上下文连写（需要提示prompt + 上下文内容context），可选参数
  "tone": "",  // 根据文本进行语调调整（需要上下文内容context），可选参数
  "topic": "",  // 根据提示进行主题书写（只需要提示prompt，不需要上下文内容context），可选参数
  "translate": "",  // 根据文本进行翻译（需要上下文内容context），可选参数
  "notion_token": "",  // notion的 token_v2值【必选参数】
  "space_id": "",  // notion的 space_id值【必选参数】
  "api_url": ""  // 代理的api url，可选参数
}
```

### 接口访问
默认接口请求路径：`/ai/notion`
请求方式：POST

接口请求示例请求查看：[notionai-api接口示例](https://console-docs.apipost.cn/preview/c31f8e11d6996f27/9832b4a0bb359b4e)
![notionai-api-接口请求示例](/screenshots/notionai-api-demo.png)


### Gradio-UI
[点击这里查看Gradio-UI的README.md](gradio_ui/README.md)
![gradio_ui](/screenshots/gradio-ui.png)


### 技术交流
- [Join Discord >>](https://discord.com/invite/eRuSqve8CE)
- WeChat：`SamgeApp`


### 免责声明
该程序仅供技术交流，使用者所有行为与本项目作者无关
