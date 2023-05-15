from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os 

def _main():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    
    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        options=options
    )
    try:
        driver.get('https://app.microcms.io/signin')
        # ユーザー名とパスワードの入力フィールドを見つける
        email_field = driver.find_element(By.NAME, 'email')  
        password_field = driver.find_element(By.NAME, 'password')  
        # ユーザー名とパスワードを入力
        email = os.environ.get('EMAIL')
        password = os.environ.get('PASSWORD')
        email_field.send_keys(email)
        password_field.send_keys(password)
        time.sleep(1)
        # ログインボタンをクリック
        login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div/div/div/div[2]/div[1]/button')
        login_button.click()
        time.sleep(3)
        # ブログをクリック
        element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div/div/div/table/tbody/tr')
        element.click()
        time.sleep(3)
        # 新規作成をクリック
        link = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div/main/div/div/div[1]/div[2]/a')
        link.click()
        time.sleep(2)
        # タイトルと本文を入力
        title = driver.find_element(By.TAG_NAME,'input')
        contents = driver.find_element(By.CLASS_NAME,'ql-editor')
        title.send_keys('test title')
        contents.send_keys('test contents')
        time.sleep(1)
        # 保存をクリック
        openBlog = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div/main/div/div/div[1]/div[2]/button[2]')
        openBlog.click()
        time.sleep(1)
        # ブログを確認をクリック
        Alert(driver).accept()
        print('ブログ記事を投稿しました。')
    except Exception as e:
        print('エラー：',e)
    finally:
        driver.quit()
if __name__ == '__main__':
    _main()