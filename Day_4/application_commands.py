from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

original_title = "OrangeHRM"
driver.get("https://opensource-demo.orangehrmlive.com")
page_title = driver.title
print(f"page_title : {page_title}")
assert page_title == original_title, f"title not matched" 

current_url = driver.current_url
print(f"current_url : {current_url}")

page_source = driver.page_source
print(f"page_source : {page_source}")



