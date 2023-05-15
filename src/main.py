from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
import os


def create_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    return webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        options=options
    )


def login(driver, email, password):
    driver.get('https://app.microcms.io/signin')
    driver.find_element(By.NAME, 'email').send_keys(email)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div/div/div/div[2]/div[1]/button').click()


def create_new_blog_post(driver):
    driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div/div/div/table/tbody/tr').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/main/div/div/div[1]/div[2]/a').click()
    time.sleep(2)
    driver.find_element(By.TAG_NAME, 'input').send_keys('test title')
    driver.find_element(By.CLASS_NAME, 'ql-editor').send_keys('test contents')
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/main/div/div/div[1]/div[2]/button[2]').click()
    time.sleep(1)
    Alert(driver).accept()


def main():
    driver = None
    try:
        driver = create_webdriver()
        login(driver, os.getenv('EMAIL'), os.getenv('PASSWORD'))
        time.sleep(3)
        create_new_blog_post(driver)
        print('ブログ記事を投稿しました。')
    except NoSuchElementException as e:
        print('エラー：', e)
        if driver:
            print('エラーが発生したURL：', driver.current_url)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            driver.save_screenshot(f'../error/error-{timestamp}.png')
    except Exception as e:
        print('未知のエラー：', e)
        if driver:
            print('エラーが発生したURL：', driver.current_url)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            driver.save_screenshot(f'../error/error-{timestamp}.png')
    finally:
        if driver:
            driver.quit()


if __name__ == '__main__':
    main()
