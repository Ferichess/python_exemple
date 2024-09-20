from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

csv_file = "CSVdata.csv"
test_data = []
with open(csv_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        test_data.append(row)
print("data csv :", test_data)

for row in test_data:
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(5)
    website = "https://www.saucedemo.com/"
    driver.get(website)
    driver.find_element(By.ID, value="user-name").send_keys(row["username"])
    driver.find_element(By.ID, value="password").send_keys(row["password"])
    driver.find_element(By.ID, value="login-button").click()
    time.sleep(5)
    driver.quit()
