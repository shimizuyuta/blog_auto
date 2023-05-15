# ブログ記事の自動生成・自動投稿
GPTに生成させた記事をMicroCMSにログインして記事を投稿してくれる(GPTとの連携は今後実装予定)

# 手順

1. アクセスURL： http://localhost:7900  
![image](https://github.com/shimizuyuta/blog_auto/assets/58338829/2268d2df-2e8a-46e5-940f-398681041b91)
2. 接続をクリック

![image](https://github.com/shimizuyuta/blog_auto/assets/58338829/e17ce38a-c5d6-41f0-b1a7-30db2ad84dd6)

3. defaultで設定されるパスワード：secretを入力
![image](https://github.com/shimizuyuta/blog_auto/assets/58338829/389f088e-1b52-492d-a5b0-81f79021a3db)

4. コードを実行させる
```python :python
python src/main.py
```
--- 

# デモ
### 正常時：

### 異常時:
スクリンショットがerrorディレクトリに格納され、メッセージがログに出力される仕様
<img width="901" alt="image" src="https://github.com/shimizuyuta/blog_auto/assets/58338829/3e293825-d20d-43cb-8ca1-b1458f008b00">
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
- 今回はdocker-seleniumのイメージを使用しましたが、DockerfileからChrome,Chromedriverを入れてやるやり方もあります。 [ChromeDriveの公式インストール](https://chromedriver.chromium.org/downloads)
- http://localhost:4444 はGrid（Selenium Server）を表し、これを介してブラウザの自動化操作をコントロールする。
- http://localhost:7900 はSeleniumのStandalone Chromeイメージで利用され、ライブブラウザセッションを視覚的にデバッグするためのVNCビューワーを提供
