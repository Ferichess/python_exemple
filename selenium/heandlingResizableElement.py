from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
website = "https://demo.automationtesting.in/Resizable.html"
driver.get(website)

resizable_element = driver.find_element(
    By.XPATH,
    value="//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']",
)
initial_element = driver.find_element(By.XPATH, value="//div[@id='resizable']")
initial_size = initial_element.size
print("initial size", initial_size)
time.sleep(5)
actions = ActionChains(driver)
actions.click_and_hold(resizable_element).move_by_offset(
    xoffset=200, yoffset=200
).release().perform()
time.sleep(5)
resized_element = initial_element.size
print("resized Element", resized_element)
time.sleep(5)
driver.quit()
