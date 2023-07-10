import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://money.rediff.com/gainers/bse/groupa")

# self::tag_name - element itself
text_T1 = driver.find_element(By.XPATH, "//a[contains(text(), 'Sun Pharma Advanced')]/self::a").text
print(f"text_T1 = {text_T1}")

# parent::tag_name - tag_name just before self element
text_T2 = driver.find_element(By.XPATH, "//a[contains(text(), 'IFCI Ltd')]/parent::td").text
print(f"text_T2 = {text_T2}")

# child::tag_name (after ancestor or after parent tag)
text_T3 = driver.find_elements(By.XPATH, "//a[contains(text(), 'Inox Wind Ltd')]/ancestor::tr//child::td")
print(f"number of nodes in text_T3 = {len(text_T3)}")

for t in text_T3:
    print(t.text)


# ancestor::tag_name - (just before parent tag, it will return all the child element at once)
text_T4 = driver.find_element(By.XPATH, "//a[contains(text(), 'Ashoka Buildcon Ltd')]/ancestor::tr").text
print(f"text_T4 = {text_T4}")


# descendant::tag_name - (just after self node, it will return all the below of self element at once inside self tag)
text_T5 = driver.find_elements(By.XPATH, "//a[contains(text(), 'Ashoka Buildcon Ltd')]/ancestor::tr/descendant::td")
print(f"number of nodes in text_T5 = {len(text_T5)}")


# following::tag_name - (it will return all the tags or even tags under tags after self node)
text_T6 = driver.find_elements(By.XPATH, "//a[contains(text(), 'Ashoka Buildcon Ltd')]/ancestor::tr/following::*")
print(f"number of nodes in text_T6 = {len(text_T6)}")


# following-sibling::tag_name - (it will return only sibling tags)
text_T7 = driver.find_elements(By.XPATH, "//a[contains(text(), 'Ashoka Buildcon Ltd')]/ancestor::tr/following-sibling::*")
print(f"number of nodes in text_T7 = {len(text_T7)}")


# preceding::tag_name - (it will return all the tags or even tags under tags before self node)
text_T8 = driver.find_elements(By.XPATH, "//a[contains(text(), 'Ashoka Buildcon Ltd')]/ancestor::tr/preceding::*")
print(f"number of nodes in text_T8 = {len(text_T8)}")


# preceding-sibling::tag_name - (it will return all the tags or even tags under tags before self node)
text_T9 = driver.find_elements(By.XPATH, "//a[contains(text(), 'Ashoka Buildcon Ltd')]/ancestor::tr/preceding-sibling::*")
print(f"number of nodes in text_T9 = {len(text_T9)}")

