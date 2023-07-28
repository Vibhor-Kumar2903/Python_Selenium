import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")

driver.find_element(By.LINK_TEXT, "Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Digital")

total_links = driver.find_elements(By.XPATH, "//a")
print(f"Total number of links : {len(total_links)}")

for link in total_links:
    print(link.text)
