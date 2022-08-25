from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path = "C:\Development\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
total = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(total.text)
