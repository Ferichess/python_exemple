from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
website = "https://the-internet.herokuapp.com/javascript_alerts"
driver.get(website)

# opsi 1 alert
# alertButton = driver.find_element(
#     By.XPATH, value="//button[normalize-space()='Click for JS Alert']"
# )

# opsi 2 alert
# alertButton = driver.find_element(
#     By.XPATH, value="//button[normalize-space()='Click for JS Confirm']"
# )

# opsi 3 alert
alertButton = driver.find_element(
    By.XPATH, value="//button[normalize-space()='Click for JS Prompt']"
)
alertButton.click()

alert = driver.switch_to.alert
alert_text = alert.text

print("alert text : ", alert_text)


alert.send_keys("this is selenium with python tutorial on handling alerts")

time.sleep(5)


# opsi accept or dismiss
alert.accept()
# alert.dismiss()


time.sleep(5)
driver.close()
