from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import pickle,time, yaml, os


def markdownToPPT():
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
        print('打開瀏覽器')
        driver = webdriver.Chrome('./driver/chromedriver.exe', options=options)
        driver.set_page_load_timeout(30)
        driver.get('https://www.mindshow.fun/')
        localstorage = yaml.safe_load(open('local_storage.yml'))
        for key, value in localstorage.items():
            driver.execute_script("localStorage.setItem(arguments[0],arguments[1]);", key, value)
    
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies: 
            driver.add_cookie(cookie)
        time.sleep(3)
        print('匯入登入資訊')
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
    except Exception as E:
        print(f'異常: {E}')
        driver.close()
        markdownToPPT()
    finally:
        driver.close()
