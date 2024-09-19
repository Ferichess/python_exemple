import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")
driver.maximize_window()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
checkboxes = driver.find_elements(By.XPATH, value="//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)
    time.sleep(2)

check_count = 0
for checkbox in checkboxes:
    if checkbox.is_selected():
        check_count += 1
expected_check_count = len(checkboxes)

if check_count == expected_check_count:
    print("checkboxes count verified")
else:
    print("checkboxes count mismatch")

# opsi single checkbox
# driver.find_element(
#     By.XPATH,
#     value="//label[normalize-space()='Sunday']",
# ).click()


time.sleep(5)
driver.close()
