# Python image to use.
FROM python:3.7

# Install dependencies.
COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONIOENCODING utf-8
ENV TZ="Asia/Tokyo"
ENV LANG=C.UTF-8
ENV LANGUAGE=en_US:en_US
# Set display port to avoid crash.
# ワーキングディレクトリを設定
WORKDIR /app

# アプリケーションのコードをコピー
COPY ./src /app
