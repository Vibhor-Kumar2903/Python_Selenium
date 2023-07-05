import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()


driver.get("https://demo.nopcommerce.com/")

# By ID
# driver.find_element(By.ID, 'small-searchterms').send_keys('Apple')

# By NAME
driver.find_element(By.NAME, 'q').send_keys('Apple')

# By Link text
# driver.find_element(By.LINK_TEXT, 'Register').click()

# By Partial link text
# driver.find_element(By.PARTIAL_LINK_TEXT, 'Regis').click()

# By class name
menu = driver.find_elements(By.CLASS_NAME, 'header-menu')
print(len(menu))

links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))


time.sleep(5)





