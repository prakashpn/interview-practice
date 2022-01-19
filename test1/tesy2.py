from selenium import webdriver
import time
import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# print(sys.path)

# firefox_export_PATH = r'D:/seleum_driver/geckodriver.exe'
chrome_export_PATH = r'D:/seleum_driver/chromedriver.exe'

# search_terms = ["elastic search", "vue tutorial"]
search_terms = ["data analysist", "pythn tutorial", "pandas tutorial"]

count = 0
while count < 300:
    for term in search_terms:
        ser = Service(chrome_export_PATH)
        op = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=ser, options=op)

        driver.maximize_window()
        driver.get("https://www.google.co.in/")

        driver.execute_script(f"document.body.style.zoom='50%'")

        search = driver.find_element(By.NAME, "q")
        time.sleep(5)
        search.clear()
        print("term -> ", term)

        search.send_keys(term)
        search.send_keys(Keys.RETURN)

        time.sleep(5)
        assert "No results found." not in driver.page_source
        driver.find_element(By.XPATH, '(//h3)[1]/../../a').click()

        time.sleep(5)
        driver.close()
        time.sleep(240)
        print("before count -> ", count)
        count = count + 1
        print("after count -> ", count)

else:
    pass
