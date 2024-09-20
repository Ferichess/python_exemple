from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome()
driver.maximize_window()
website = "https://the-internet.herokuapp.com/drag_and_drop"
driver.get(website)
source_element = driver.find_element(By.ID, value="column-a")
destination_element = driver.find_element(By.ID, value="column-b")
actions = ActionChains(driver)
actions.drag_and_drop(source_element, destination_element).perform()
time.sleep(5)
driver.quit()
