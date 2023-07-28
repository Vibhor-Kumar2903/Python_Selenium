import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://itera-qa.azurewebsites.net/home/automation")

# select a single checkbox
monday = driver.find_element(By.ID, "monday")
monday.click()
time.sleep(3)
monday.click()
time.sleep(3)


# select multiple checkbox
check_box = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
print(f"Number of checkbox found : {len(check_box)}")

selected = []

for box in check_box:
    box.click()
    time.sleep(1)
    print(f"{box.get_attribute('id')} checked.")

    if box.is_selected():
        selected.append(box.get_attribute('id'))

assert len(selected) == len(check_box), f"Missing check_box"

print(f"Selected checkbox : {selected}")


# deselect
for i in range(len(check_box)):
    if check_box[i].is_selected():
        check_box[i].click()
        time.sleep(1)

    if not check_box[i].is_selected():
        print(f"{check_box[i].get_attribute('id')} is de_selected.")


# select_first_two_checkbox
for i in range(len(check_box)):
    if i < 2:
        check_box[i].click()

# deselect_first_two_checkbox
for i in range(len(check_box)):
    if i < 2:
        check_box[i].click()
