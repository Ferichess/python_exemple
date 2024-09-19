from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.maximize_window()
website = "https://selenium.dev/"
driver.get(website)
driver.switch_to.new_window()
driver.get("https://playwright.dev/")
number_of_tabs = len(driver.window_handles)
print(f"number of tabs : {number_of_tabs}")
tabs_values = driver.window_handles
print(f"tabs values : {tabs_values}")
current_tab = driver.current_window_handle
print(f"current tab : {current_tab}")
driver.find_element(By.CSS_SELECTOR, value=".getStarted_Sjon").click()
time.sleep(5)
first_tab = driver.window_handles[0]
if current_tab != first_tab:
    driver.switch_to.window(first_tab)
driver.find_element(By.XPATH, value="//a[@href='/downloads']").click()

time.sleep(5)
driver.close()
