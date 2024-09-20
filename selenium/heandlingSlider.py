from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
website = "https://the-internet.herokuapp.com/horizontal_slider"
driver.get(website)
slider = driver.find_element(By.XPATH, value="//input[@type='range']")
actions = ActionChains(driver)
actions.click_and_hold(slider).move_by_offset(xoffset=35, yoffset=0).release().perform()
time.sleep(5)
driver.quit()
