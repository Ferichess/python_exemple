from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
website = "https://www.saucedemo.com/"
driver.get(website)
driver.find_element(By.ID, value="user-name").send_keys("standard_user")
driver.find_element(By.ID, value="password").send_keys("secret_sauce")
driver.find_element(By.ID, value="login-button").click()

driver.find_element(By.ID, value="//button[@id='react-burger-menu-btn']").click()
driver.find_element(By.ID, value="//a[@id='logout_sidebar_link']").click()
driver.close()
