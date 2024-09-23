from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.google.com/recaptcha/api2/demo")

driver.find_element(By.ID, value="recaptcha-anchor").click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "recaptcha-audio-button"))
).click()
