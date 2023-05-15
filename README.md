# ブログ記事の自動生成・自動投稿
GPTに生成させた記事をMicroCMSにログインして記事を投稿してくれる

# 環境
- MackBookPro 2022 M2 
- macOS Ventura 13.2.1
- Docker
- Chrome Version 112.0.5615.137(Official Build)(arm64)
  
# 環境構築
### 1. .envの設定
```bash
EMAIL=MicroCMSに登録しているメールアドレスを指定
PASSWORD=MicroCMSに登録しているパスワードを指定
```
### 2. Dockerイメージビルド
```bash
docker-compose build --no-cache
```
### 3. Dockerコンテナ起動
```bash
docker-compose up -d 
```
### 4. Dockerコンテナ・イメージ削除
```bash :削除コマンド
docker-compose down --rmi all --volumes --remove-orphans
```

# 備考
-　今回はdocker-seleniumのイメージを使用しましたが、DockerfileからChrome,Chromedriverを入れてやるやり方もあります。 [ChromeDriveの公式インストール](https://chromedriver.chromium.org/downloads)
