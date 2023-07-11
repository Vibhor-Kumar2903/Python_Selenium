import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://demo.nopcommerce.com")

search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
search_box.send_keys("Apple")

link_1 = driver.find_element(By.XPATH, "//div[@class='footer']//a")
print(f"link_1 : {link_1.text}")

links = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
print(links)
print(len(links))
print(links[0].text)

for lt in links:
    print(lt.text)

element = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
print(len(element))

element[0].send_keys("Apple macbook Pro")


