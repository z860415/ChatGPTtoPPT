from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests, pickle, time
import yaml


try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_page_load_timeout(30)
    driver.get('https://www.mindshow.fun/#/login')
    account_input = driver.find_element(By.XPATH,'//*[@id="login_tab"]/div[1]/div[3]/div/div[4]/div[1]/input')
    account_input.send_keys('z860415@gmail.com')
    time.sleep(3)
    submit_button = driver.find_element(By.XPATH, '//*[@id="login_tab"]/div[1]/div[3]/div/div[4]/div[2]')
    submit_button.click()
    time.sleep(10)
    password_input = driver.find_element(By.XPATH, '//*[@id="loginEmailPassword"]')
    password_input.send_keys('z800525')
    time.sleep(3)
    submit_button = driver.find_element(By.XPATH, '//*[@id="app"]/section/div[2]/div/div[1]/div[5]')
    submit_button.click()
    time.sleep(10)
    request = requests.Session()
    headers = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"}
    request.headers.update(headers)
    cookies = driver.get_cookies()
    pickle.dump(cookies, open('cookies.pkl', 'wb'))
    local_storage = driver.execute_script("return window.localStorage")
    with open('local_storage.yml', "w") as f:
    # 第一个参数是要写入的数据，第二个字段是要进行数据操作的资源文件
        yaml.safe_dump(local_storage, f)
        print("保存成功")
    time.sleep(10)
except:
    pass
finally:
    driver.close()
