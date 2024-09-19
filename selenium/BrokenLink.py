from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests

driver = webdriver.Firefox()
driver.maximize_window()
website = "https://jqueryui.com/"
driver.get(website)

all_links = driver.find_elements(By.TAG_NAME, value="a")
print(f"Total number of links on the page : {len(all_links)}")

for link in all_links:
    href = link.get_attribute("href")
    response = requests.get(href)
    if response.status_code >= 400:
        print(f"broken link : {href} (status code : {response.status_code})")
    else:
        print(f"good link : {href} (status code : {response.status_code})")


time.sleep(5)
driver.close()
