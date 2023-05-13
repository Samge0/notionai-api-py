## NotionAI Api相关的Gradio操作工具界面

### docker方式运行

[点击这里查看docker说明](../docker/gradio/README.md)


### 本地源码运行

- 安装依赖
```shell
pip install -r requirements.txt
pip install -r gradio_ui/requirements.txt
```

- 运行（直接运行gradio_ui/app.py，或者：）
```shell
uvicorn gradio_ui.app:app --host 0.0.0.0 --port 7860
```


![gradio_ui](/screenshots/gradio-ui.png)