from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, pickle
import yaml
import os


MINDSHOW_ACCOUNT = os.getenv('MINDSHOW_ACCOUNT')
MINDSHOW_PASSWORD = os.getenv('MINDSHOW_PASSWORD')

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(10)

try:
    driver.get('https://www.mindshow.fun/#/login')
    account_input = driver.find_element(By.XPATH, '//*[@id="login_tab"]/div[1]/div[3]/div/div[4]/div[1]/input')
    account_input.send_keys(MINDSHOW_ACCOUNT)
    submit_button = driver.find_element(By.XPATH, '//*[@id="login_tab"]/div[1]/div[3]/div/div[4]/div[2]')
    submit_button.click()
    password_input = driver.find_element(By.XPATH, '//*[@id="loginEmailPassword"]')
    password_input.send_keys(MINDSHOW_PASSWORD)
    submit_button = driver.find_element(By.XPATH, '//*[@id="app"]/section/div[2]/div/div[1]/div[5]')
    submit_button.click()
    time.sleep(5)

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
