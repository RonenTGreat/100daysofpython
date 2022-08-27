from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:\Development\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
products = driver.find_elements(By.CSS_SELECTOR, "#rightPanel b")[:-1]
all_products = [p.text.split("-")[0].strip() for p in products]

five_sec = time.time() + 5
five_min = time.time() + 60 * 2

while True:
    cookie.click()
    if time.time() > five_sec:
        grayed_products = driver.find_elements(By.CSS_SELECTOR, ".grayed b")
        not_available_products = [p.text.split("-")[0].strip() for p in grayed_products]
        available_products = [p for p in all_products if p not in not_available_products]
        print("available products: ", available_products)
        if len(available_products) > 0:
            buy = available_products[-1]
            buy_product = driver.find_element(By.ID, f'buy{buy}')
            buy_product.click()
            print(f'just bought {buy}')

        five_sec = time.time() + 5

    if time.time() > five_min:
        cookie_per_sec = driver.find_element(By.ID, "cps").text
        print(cookie_per_sec)
        break
