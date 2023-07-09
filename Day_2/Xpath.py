from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")
driver.find_element(By.CSS_SELECTOR, "img[alt='nopCommerce demo store']")

text1 = driver.find_element(By.XPATH, "//div/ul/li/a[text()='Digital downloads ']")
print(text1.text)

text2 = driver.find_element(By.XPATH, "//h2/a[contains(text(), 'Electro')]")
print(text2.text)

# starts-with() function only works for attributes
text3 = driver.find_element(By.XPATH, "//button[starts-with(@class, 'button-1')]")
print(text3.text)

text4 = driver.find_element(By.XPATH, "//h2/a[text()[normalize-space() = 'Apparel')]")
print(text4.text)
# text5 = driver.find_element(By.XPATH, "//h2/a[normalize-space(text()) = 'Apparel')]")
# print(text5.text)

# //div[text()[normalize-space() = 'space in between']]
# //div[normalize-space(text()) = 'space in between']
# //div[normalize-space(@class)='my class 1']
# //div[contains(normalize-space(),'Apparel')]
# //div[contains(normalize-space(@class),'my class')]
