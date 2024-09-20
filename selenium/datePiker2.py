from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
from datetime import datetime, timedelta

driver = webdriver.Chrome()
driver.maximize_window()
website = "https://demo.automationtesting.in/Datepicker.html"
driver.get(website)
driver.find_element(By.ID, value="datepicker2").click()
time.sleep(5)
current_date = datetime.now()
print(current_date)

next_day = current_date + timedelta(days=1)
NextDay = str(next_day.day)
print(NextDay)

current_month = datetime.now().month
current_year = datetime.now().year

next_month = (current_month % 12) + 1

next_month_year = f"{next_month}/{current_year}"

Month_Dropdown = driver.find_element(
    By.CSS_SELECTOR, value="select[title='Change the month']"
)
select = Select(Month_Dropdown)
select.select_by_value(str(next_month_year))

year_dropdown = driver.find_element(
    By.CSS_SELECTOR, value="select[title='Change the year']"
)

select_year = Select(year_dropdown)
select_year.select_by_visible_text("2023")

driver.find_element(By.LINK_TEXT, NextDay).click()

time.sleep(5)

driver.quit()
