import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(20)

original_title = "OrangeHRM"
driver.get("https://opensource-demo.orangehrmlive.com")

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
time.sleep(5)


