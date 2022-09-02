from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = r"C:\Development\chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
