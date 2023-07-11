import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://admin-demo.nopcommerce.com/login")

email = driver.find_element(By.CSS_SELECTOR, '#Email')
email.clear()

time.sleep(5)
email.send_keys("abc@gmail.com")

value = email.get_attribute('value')
print(f"value : {value}")
time.sleep(5)


button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
button_text = button.text
print(f"button_text : {button_text}")

button_type = button.get_attribute('type')
print(f"button_type : {button_type}")



