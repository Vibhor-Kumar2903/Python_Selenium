import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.amazon.in/")
driver.get("https://www.snapdeal.com/")
time.sleep(5)

driver.back()
time.sleep(5)

driver.forward()
time.sleep(5)

driver.refresh()
time.sleep(5)

driver.quit()
