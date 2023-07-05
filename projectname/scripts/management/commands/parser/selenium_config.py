from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path = r'C:\sequencer\fullstack_django\webdr\chromedriver.exe'


def get_html(url):

    options = Options()
    # options.add_argument('--headless')  # Запуск браузера в фоновом режиме

    driver = webdriver.Chrome(service=Service(driver_path), options=options)
    driver.get(url)

    wait = WebDriverWait(driver, 100)  # Ожидание, пока страница полностью загрузится

    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'products-list-v2__item')))

    height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.1)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == height:
            break
        
        height = new_height

    html = driver.page_source

    driver.quit()

    return html