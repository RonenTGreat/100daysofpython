from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = r"C:\Development\chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.ronenhammond.me")
driver.implicitly_wait(5)
my_element = driver.find_element(By.CLASS_NAME, "cta-resume")
my_element.click()
