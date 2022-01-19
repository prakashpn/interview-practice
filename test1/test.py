from selenium import webdriver
import time
import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# print(sys.path)

# firefox_export_PATH = r'D:/seleum_driver/geckodriver.exe'
chrome_export_PATH = r'D:/seleum_driver/chromedriver.exe'

# search_terms = ["elastic search", "vue tutorial"]
search_terms = ["data analysist", "pythn tutorial","pandas tutorial"]

count = 0
while count < 300:
    for term in search_terms:
        # driver = webdriver.Firefox(executable_path=firefox_export_PATH)
        driver = webdriver.Chrome(executable_path=chrome_export_PATH)
        # driver.set_window_size(1000, 1000)
        driver.get("https://www.google.co.in/")
        # driver.execute_script("$('#values').scss('zoom', 50%);")
        driver.execute_script(f"document.body.style.zoom='50%'")
        # driver.execute_script("document.body.style.transform = 'scale(0.8)'")

        search = driver.find_element_by_name("q")
        time.sleep(5)
        search.clear()
        print("term -> ", term)

        search.send_keys(term)
        search.send_keys(Keys.RETURN)

        time.sleep(5)
        assert "No results found." not in driver.page_source
        # result = driver.find_element_by_xpath('(//div[@class="r"]/a)[1]').click()
        # driver.find_element_by_xpath('("//div/h3/a)[1]').click()
        # driver.find_element_by_css_selector("div.r a h3").click()
        driver.find_element(By.XPATH, '(//h3)[1]/../../a').click()

        # result[0].click()
        time.sleep(5)
        driver.close()
        time.sleep(60)
        print("before count -> ", count)
        count = count + 1
        print("after count -> ", count)

else:
    pass
