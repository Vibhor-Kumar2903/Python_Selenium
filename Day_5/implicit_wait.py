import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.google.com/")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("selenium")
search_box.submit()

driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()
page_title = driver.title
print(page_title)
