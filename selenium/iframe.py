from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.maximize_window()
website = "https://the-internet.herokuapp.com/iframe"
driver.get(website)
iframe = driver.find_element(By.ID, value="mce_0_ifr")
driver.switch_to.frame(iframe)
text_editor = driver.find_element(By.ID, value="tinymce")
text_editor.clear()
text_editor.send_keys(" theis is selenium with python iframe tutrorial")
driver.switch_to.default_content()
selenium_link = driver.find_element(
    By.XPATH, value="//a[normalize-space()='Elemental Selenium']"
).click()


time.sleep(5)
driver.close()
