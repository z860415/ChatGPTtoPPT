from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle,time, yaml


def markdownToPPT():
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.set_page_load_timeout(30)
        driver.get('https://www.mindshow.fun/')
        localstorage = yaml.safe_load(open('local_storage.yml'))
        for key, value in localstorage.items():
            driver.execute_script("localStorage.setItem(arguments[0],arguments[1]);", key, value)
    
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies: 
            driver.add_cookie(cookie)
        driver.get('https://www.mindshow.fun/#/folder/import')
        a = input('點擊繼續')
        text_area = driver.find_element(By.XPATH,'//*[@id="my_import"]/div[3]/div[3]/textarea')
        with open('output.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        text_area.send_keys(content)
        import_button = driver.find_element(By.XPATH, '//*[@id="my_import"]/div[3]/div[3]/button')
        import_button.click()
    except Exception as E:
        print(E)
    finally:
        driver.close()

if __name__ == "__main__":
    markdownToPPT()
