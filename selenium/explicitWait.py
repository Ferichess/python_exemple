from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

driver.maximize_window()
website = "https://www.saucedemo.com/"
driver.get(website)
driver.find_element(By.ID, value="user-name").send_keys("standard_user")
driver.find_element(By.ID, value="password").send_keys("secret_sauce")
driver.find_element(By.ID, value="login-button").click()

driver.find_element(By.XPATH, value="//button[@id='react-burger-menu-btn']").click()


element = (
    WebDriverWait(driver, timeout=10)
    .until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
    .click()
)

time.sleep(5)
driver.close()
