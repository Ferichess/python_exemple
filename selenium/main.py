from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

service = Service(log_path="chromedriver.log")  # Simpan log ke file
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.google.com")
input("Press Enter to close the browser...")
