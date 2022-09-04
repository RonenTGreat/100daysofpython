import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

chrome_driver_path = r"C:\Development\chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.techwithtim.net/")
driver.implicitly_wait(5)

search = driver.find_element(By.NAME, "s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()