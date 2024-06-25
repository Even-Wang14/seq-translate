FROM python:3.9-slim
 
WORKDIR /app
# 表示把当前文件下的所有内容复制到/app文件夹下
COPY . /app
# 安装支持
RUN /usr/local/bin/python -m pip install --upgrade pip \
    # && wget https://http.kali.org/kali/pool/main/k/kali-archive-keyring/kali-archive-keyring_2024.1_all.deb --no-check-certificate \
    # && apt install ./kali-archive-keyring_2024.1_all.deb \
    && apt update \
    && apt-get install -y gnupg2 \
    && apt-get install -y gcc \
    && pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple 
 
# 设置app文件夹是工作目录


# 暴露应用端口
EXPOSE 5000
WORKDIR /app/flask
 
# 配置启动docker后自动运行的文件
CMD [ "python", "app.py" ]
