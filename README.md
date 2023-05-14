# ブログ記事の自動生成・自動投稿
GPTに生成させた記事をMicroCMSにログインして記事を投稿してくれる

# 環境
- MackBookPro 2022 M2 
- macOS Ventura 13.2.1
- Docker
- Chrome Version 112.0.5615.137(Official Build)(arm64)

# インストール
- [ChromeDriveの公式インストール](https://chromedriver.chromium.org/downloads)（自分のchromeのバージョンと同じものをインストール）
  
# 環境構築
### 1. Dockerイメージビルド
```bash
docker build --no-cache --rm -t selenium-chrome .
```
### 2. Dockerコンテナ起動
```bash
docker run -it --rm selenium-chrome bash
```
### 3. 必要なライブラリインストール
- selenium



docker-compose down --rmi all --volumes --remove-orphans
