from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
username = "27captain.potato@gmail.com"
passw = "bersihrapi"
driver.maximize_window()
driver.get("https://mail.google.com")
driver.find_element(By.ID, value="identifierId").send_keys(username)
driver.find_element(By.XPATH, value='//*[@id="identifierNext"]/div/button').click()
driver.implicitly_wait(10)
driver.find_element(By.NAME, value="password").send_keys(passw)
driver.find_element(By.XPATH, value='//*[@id="passwordNext"]/div/button').click()
print("login success")
