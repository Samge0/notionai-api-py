# 设置基础镜像
FROM python:3.10-slim-buster

# 将工作目录设置为 /app
WORKDIR /app

# 复制当前目录中的所有文件到 /app
COPY . .

# 安装所需的 Python 包（这里的all_proxy需要替换为你的代理或者删掉）
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -r gradio_ui/requirements.txt

# 声明容器监听的端口
EXPOSE 7860

# 映射缓存目录
VOLUME /app/gradio_cache

# 运行应用程序
CMD ["sh", "-c", "uvicorn gradio_ui.app:app"]
