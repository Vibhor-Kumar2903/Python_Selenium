from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome())

driver.maximize_window()

driver.get("https://www.google.com/")