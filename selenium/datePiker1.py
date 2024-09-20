from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime, timedelta

driver = webdriver.Chrome()
driver.maximize_window()
website = "https://www.globalsqa.com/demo-site/datepicker/"
driver.get(website)
driver.find_element(
    By.XPATH,
    value="//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//a[@class='close_img']",
).click()
frameLo = driver.find_element(
    By.XPATH, value="//iframe[@class='demo-frame lazyloaded']"
)
driver.switch_to.frame(frameLo)
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, value="#datepicker").click()

current_date = datetime.now()

next_date = current_date + timedelta(days=-2)

formatted_date = next_date.strftime("%m/%d/%y")

driver.find_element(By.CSS_SELECTOR, value="#datepicker").send_keys(
    formatted_date + Keys.TAB
)
time.sleep(5)
driver.close()
