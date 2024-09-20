from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome()
driver.maximize_window()
website = "https://demo.automationtesting.in/Datepicker.html"
driver.get(website)
actions = ActionChains(driver)
hover_element = driver.find_element(
    By.XPATH,
    value="//a[normalize-space()='SwitchTo']",
)
time.sleep(5)
actions.move_to_element(hover_element).perform()
driver.find_element(By.XPATH, value="//a[normalize-space()='Frames']").click()

time.sleep(5)
driver.quit()
