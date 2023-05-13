## NotionAI 的api-docker镜像
一个页面NotionAI 的api-docker镜像

### 构建api正式包
```shell
docker build . -t samge/notionai-api-py -f docker/Dockerfile
```

### 上传
```shell
docker push samge/notionai-api-py
```

### 运行docker镜像
如果 `ACCESS_TOKEN` 环境变量跟 `config.json` 同时配置，优先读取环境变量`ACCESS_TOKEN`的值

`方式1：以配置 ACCESS_TOKEN 环境变量方式运行
```shell
docker run -d \
--name notionai-api-py \
-e ACCESS_TOKEN=xxx \
-e NOTION_TOPIC=blogPost \
-e NOTION_TOKEN=xxx \
-e NOTION_SPACE_ID=xxx \
-e NOTION_API_URL=https://xxx.xxx.xxx \
-p 8233:8000 \
--pull=always \
--restart always \
--memory=1G \
samge/notionai-api-py:latest
```

`方式2：以config.json`映射方式运行
这里的`~/docker_data/notionai-api-py/config.json`需要替换为使用者的本地映射路径。
```shell
docker run -d \
--name notionai-api-py \
-v ~/docker_data/notionai-api-py/config.json:/app/config.json \
-p 8233:8000 \
--pull=always \
--restart always \
--memory=1G \
samge/notionai-api-py:latest
```