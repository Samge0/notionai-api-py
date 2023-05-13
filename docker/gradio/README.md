## NotionAI的gradio-docker镜像
一个NotionAI的gradio-docker镜像

### 构建api正式包
```shell
docker build . -t samge/notionai-api-py-gradio -f docker/gradio/Dockerfile
```

### 上传
```shell
docker push samge/notionai-api-py-gradio
```

### 运行docker镜像

创建缓存映射目录
```shell
mkdir -p ~/docker_data/notionai_api_py_gradio_cache
```

运行docker
如果 `ACCESS_TOKEN` 环境变量跟 `config.json` 同时配置，优先读取环境变量`ACCESS_TOKEN`的值

方式1：以配置 ACCESS_TOKEN 环境变量方式运行
```shell
docker run -d \
--name notionai-api-py-gradio \
-e ACCESS_TOKEN=xxx \
-e NOTION_TOPIC=blogPost \
-e NOTION_TOKEN=xxx \
-e NOTION_SPACE_ID=xxx \
-e NOTION_API_URL=https://xxx.xxx.xxx \
-v ~/docker_data/notionai_api_py_gradio_cache:/app/gradio_cache \
-p 7860:7860 \
--pull=always \
--restart always \
samge/notionai-api-py-gradio:latest
```

方式2：以config.json映射方式运行
这里的`~/docker_data/notionai-api-py/config.json`需要替换为使用者的本地映射路径。
```shell
docker run -d \
--name notionai-api-py-gradio \
-v ~/docker_data/notionai-api-py/config.json:/app/config.json \
-v ~/docker_data/notionai_api_py_gradio_cache:/app/gradio_cache \
-p 7860:7860 \
--pull=always \
--restart always \
samge/notionai-api-py-gradio:latest
```