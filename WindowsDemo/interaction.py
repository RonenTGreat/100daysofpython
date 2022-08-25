from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "C:\Development\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Ronen")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Hammond")
email = driver.find_element(By.NAME, "email")
email.send_keys("ronenh53@hotmail.com")

submit = driver.find_element(By.CSS_SELECTOR, ".btn")
submit.click()





# article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# article_count.click()

# contact_us = driver.find_element(By.LINK_TEXT, "Contact us")
# contact_us.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Computer Science")
#
# go_search = driver.find_element(By.NAME, "go")
# go_search.click()
# search.send_keys(Keys.ENTER)
