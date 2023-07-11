from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.google.com/")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("selen")
search_box.submit()

# wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
#                                                                        ElementNotVisibleException, Exception])

wait = WebDriverWait(driver, 10)

element = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
element.click()

page_title = driver.title
print(page_title)
