from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time, pickle
import yaml
import os
from dotenv import load_dotenv

load_dotenv()


MINDSHOW_ACCOUNT = os.getenv('MINDSHOW_ACCOUNT')
MINDSHOW_PASSWORD = os.getenv('MINDSHOW_PASSWORD')

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')
driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=options)
driver.set_page_load_timeout(30)

try:
    driver.get('https://www.mindshow.fun/#/login')

    waitElement = (By.XPATH,'//*[@id="login_tab"]/div[1]/div[3]/div/div[4]/div[1]/input')
    WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located(waitElement))
    account_input = driver.find_element(By.XPATH, '//*[@id="login_tab"]/div[1]/div[3]/div/div[4]/div[1]/input')
    account_input.send_keys(MINDSHOW_ACCOUNT)

    waitElement = (By.XPATH,'//*[@id="login_tab"]/div[1]/div[3]/div/div[4]/div[2]')
    WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located(waitElement))
    submit_button = driver.find_element(By.XPATH, '//*[@id="login_tab"]/div[1]/div[3]/div/div[4]/div[2]')
    submit_button.click()

    waitElement = (By.XPATH,'//*[@id="loginEmailPassword"]')
    WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located(waitElement))
    password_input = driver.find_element(By.XPATH, '//*[@id="loginEmailPassword"]')
    password_input.send_keys(MINDSHOW_PASSWORD)

    waitElement = (By.XPATH,'//*[@id="app"]/section/div[2]/div/div[1]/div[5]')
    WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located(waitElement))
    submit_button = driver.find_element(By.XPATH, '//*[@id="app"]/section/div[2]/div/div[1]/div[5]')
    submit_button.click()
    time.sleep(10)

    cookies = driver.get_cookies()
    pickle.dump(cookies, open('cookies.pkl', 'wb'))

    local_storage = driver.execute_script("return window.localStorage")
    with open('local_storage.yml', 'w') as f:
        yaml.safe_dump(local_storage, f)
        print('保存成功')
except Exception as e:
    print(e)
finally:
    driver.quit()
