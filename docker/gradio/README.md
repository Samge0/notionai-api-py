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
```shell
docker run -d \
--name notionai-api-py-gradio \
-p 7860:7860 \
-v ~/docker_data/notionai_api_py_gradio_cache:/app/gradio_cache \
--pull=always \
--restart always \
--memory=1.0G \
samge/notionai-api-py-gradio:latest
```
