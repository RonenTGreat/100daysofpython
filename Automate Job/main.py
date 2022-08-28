from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

load_dotenv()


password = os.getenv("PASSWORD")

chrome_driver_path = "C:\Development\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3228892097&f_AL=true&f_E=1%2C2&f_WT=2&geoId=103644278&"
           "keywords=html%20css&location=United%20States&refresh=true")
driver.maximize_window()

sign_in = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
sign_in.click()

time.sleep(5)
user_name = driver.find_element(By.NAME, "session_key")
user_name.send_keys(os.getenv("USER_NAME"))

password = driver.find_element(By.NAME, "session_password")
password.send_keys(os.getenv("PASSWORD"))
password.send_keys(Keys.ENTER)

time.sleep(5)
apply_button = driver.find_elements(By.CSS_SELECTOR, '.artdeco-entity-lockup__title a')
apply_button[4].click()
time.sleep(5)
apply_button = driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button--top-card button')
apply_button.click()
time.sleep(5)

input = driver.find_element(By.CSS_SELECTOR,'.artdeco-button--primary')
print(input.text)
input.click()
print('first next')
time.sleep(5)
input = driver.find_element(By.CSS_SELECTOR,'.artdeco-button--primary')
print(input.text)
input.click()
print('second next')

time.sleep(5)
input = driver.find_element(By.CSS_SELECTOR,'.artdeco-button--primary')
print(input.text)
input.click()
print('third next')

input = driver.find_element(By.CSS_SELECTOR,'.artdeco-button--primary')
print(input.text)
input.click()
print('review')

# driver.quit()
