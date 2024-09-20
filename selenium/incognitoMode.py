from selenium import webdriver

# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
import time

chrome_options = Options()
# chrome_options.add_argument("--incognito")
chrome_options.add_argument("--private")
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Firefox(options=chrome_options)
driver.maximize_window()
time.sleep(15)
website = "https://www.google.com/"
driver.get(website)

time.sleep(5)
driver.quit()
