from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3228892097&f_AL=true&f_E=1%2C2&f_WT=2&geoId=103644278&"
           "keywords=html%20css&location=United%20States&refresh=true")










driver.quit()
