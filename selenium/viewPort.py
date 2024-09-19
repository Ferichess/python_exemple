# selenium\viewPort.py
import time
from selenium import webdriver

viewPorts = [(1024, 768), (768, 1024), (375, 667), (414, 896)]
driver = webdriver.Chrome()
driver.get("https://www.google.com/")

try:
    for width, height in viewPorts:
        driver.set_window_size(width=width, height=height)
        time.sleep(5)
finally:
    driver.close()
