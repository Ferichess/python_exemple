from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.maximize_window()
website = "https://cosmocode.io/automation-practice-webtable/"
driver.get(website)
driver.execute_script("window.scrollTo(0, 700);")
table = driver.find_element(By.ID, value="countries")
rows = table.find_elements(By.TAG_NAME, value="tr")
row_count = len(rows)
print(row_count)
target_value = "Australia"
found = False
for row in rows:
    cells = row.find_elements(By.TAG_NAME, value="td")
    for cell in cells:
        if target_value in cell.text:
            print(f"found {target_value} in {cell.text}")
            found = True
            break
    if found:
        break
if not found:
    print(f"target value {target_value} not found")


time.sleep(5)
driver.close()
