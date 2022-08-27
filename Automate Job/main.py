from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

load_dotenv()


password = os.getenv("PASSWORD")

chrome_driver_path = "C:\Development\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3228892097&f_AL=true&f_E=1%2C2&f_WT=2&geoId=103644278&"
           "keywords=html%20css&location=United%20States&refresh=true")

sign_in = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
sign_in.click()

time.sleep(15)
user_name = driver.find_element(By.NAME, "session_key")
user_name.send_keys(os.getenv("USER_NAME"))

password = driver.find_element(By.NAME, "session_password")
password.send_keys(os.getenv("PASSWORD"))






# driver.quit()
