from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

username = "admin"
password = "admin"
driver = webdriver.Chrome()
driver.maximize_window()
website = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
driver.get(website)
time.sleep(5)
# https://username:pssword@domain/path

time.sleep(5)
driver.quit()
