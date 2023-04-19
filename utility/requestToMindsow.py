from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time, os
from dotenv import load_dotenv


def markdownToPPT():
    load_dotenv()
    MINDSHOW_ACCOUNT = os.getenv('MINDSHOW_ACCOUNT')
    MINDSHOW_PASSWORD = os.getenv('MINDSHOW_PASSWORD')
    try:
        work_dir = os.path.abspath(os.getcwd())
        download_button_xpath = '//*[@id="m2p_r_ppt_share_btn"]'
        pptx_link_xpath = '/html/body/div[2]/div/div/ul/li[2]/span/span[1]'
        continue_button_xpath = "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]/span"
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
            "download.default_directory": work_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=options)
        driver.set_page_load_timeout(30)
        print('開啟瀏覽器')
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
        time.sleep(3)
        print('登入成功')

        driver.get('https://www.mindshow.fun/#/folder/import')

        text_area = (By.XPATH,'//*[@id="my_import"]/div[3]/div[3]/textarea')
        WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located(text_area))
        text_area = driver.find_element(By.XPATH,'//*[@id="my_import"]/div[3]/div[3]/textarea')
        with open('output.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        text_area.send_keys(content)
        print('輸入文本')
        import_button = driver.find_element(By.XPATH, '//*[@id="my_import"]/div[3]/div[3]/button')
        import_button.click()
        print('點擊送出')
        download_button = (By.XPATH, download_button_xpath)
        WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located(download_button))
        download_button = driver.find_element(By.XPATH, download_button_xpath)
        download_button.click()
        print('點擊下載')
        pptx_link = (By.XPATH, pptx_link_xpath)
        WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located(pptx_link))
        pptx_link_button = driver.find_element(By.XPATH, pptx_link_xpath)
        pptx_link_button.click()
        print('點擊同意')
        continue_button = (By.XPATH, continue_button_xpath)
        WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located(continue_button))
        continue_button = driver.find_element(By.XPATH, continue_button_xpath)
        time.sleep(3)
        continue_button.click()
        print('點擊繼續')
        
        time.sleep(5)
        print("Waiting for downloads", end="")
        while any([filename.endswith(".crdownload") for filename in os.listdir(work_dir)]):
            time.sleep(2)
        for filename in os.listdir(work_dir):
            if filename.endswith('.pptx'):
                os.replace(filename, './download/file.pptx')
        print('下載完成')
        driver.close()
    except Exception as E:
        print(f'異常: {E}')
        driver.close()
        markdownToPPT()
