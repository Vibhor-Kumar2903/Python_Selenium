import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.facebook.com/login/")

# By CSS_SELECTOR
# tag + id -   e.g. (html_tag#id = input#id = #id)
# tag + class - e.g. (html_tag.classValue = input.classValue = .classValue)
# tag + attribute - e.g. (html_tag[attribute=value] = input[name="email"] = [name="email"])
# tag + class + attribute - e.g. (html_tag.classValue[attribute=value] = input.inputtext[name="email"] = .inputtext[name="email"])


# tag_name#id
driver.find_element(By.CSS_SELECTOR, 'input#email').send_keys("Peter")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '#email').clear()

# tag_name.classValue
driver.find_element(By.CSS_SELECTOR, 'input.inputtext').send_keys("Parker")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '.inputtext').clear()

# tag_name[attribute=value]
driver.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys("Spider")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '[name="email"]').clear()

# tag_name.classValue[attribute=value]
driver.find_element(By.CSS_SELECTOR, 'input.inputtext[name="email"]').send_keys("Man")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '.inputtext[name="email"]').clear()

time.sleep(10)






