import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/register")

search_box = driver.find_element(By.XPATH, "//button[normalize-space()='Search']")

displayed_status = search_box.is_displayed()
print(f"displayed_status : {displayed_status}")

enabled_status = search_box.is_enabled()
print(f"enabled_status : {enabled_status}")

# ------------------------------------------------------------------ #

button_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
button_male.click()
select_status_male = button_male.is_selected()
print(f"select_status_male : {select_status_male}")

button_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")
select_status_female = button_female.is_selected()
print(f"select_status_female : {select_status_female}")

time.sleep(5)
