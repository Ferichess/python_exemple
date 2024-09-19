import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.maximize_window()
website = "https://the-internet.herokuapp.com/broken_images"
driver.get(website)
images = driver.find_elements(By.TAG_NAME, value="img")
broken_images = []
for image in images:
    src = image.get_attribute("src")
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            print(f"broken image : {src} (status code : {response.status_code})")
            broken_images.append(src)
        else:
            print(f"good image : {src} (status code : {response.status_code})")
if broken_images:
    print("list od broken images")
    for broken_image in broken_images:
        print(broken_image)
else:
    print("no broken images found")


time.sleep(5)
driver.close()
