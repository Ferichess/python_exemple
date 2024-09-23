import time
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


chrome_options = Options()
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--verbose")
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=chrome_options
)
url = " https://setcookie.net/"

driver.get(url)

try:
    with open("cookies.pkl", "rb") as f:
        cookies = pickle.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get(url)
except FileNotFoundError:
    print("cookies not found")

    time.sleep(5)
    name_input = driver.find_element(By.NAME, value="name")
    value_input = driver.find_element(By.NAME, value="value")

    name_input.send_keys("somecookiename")
    value_input.send_keys("somecookievalue")

    submit_button = driver.find_element(
        By.XPATH, value="//input[@type='submit']"
    ).click()

    time.sleep(5)

with open("cookies.pkl", "wb") as f:
    pickle.dump(driver.get_cookies(), f)

driver.get(url)
time.sleep(5)

driver.quit()
