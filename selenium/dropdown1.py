import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
login_url = "https://the-internet.herokuapp.com/dropdown"
driver.get(login_url)
driver.maximize_window()
dropdown = driver.find_element(By.ID, value="dropdown")


select = Select(dropdown)

# opsi select the value by visible text
# select.select_by_visible_text("Option 2")
# opsi select the value by index
# select.select_by_index(1)
# opsi select the option by using a value
# select.select_by_value("2")

# option_count = len(select.options)
# expected_count = 5

# if option_count == expected_count:
#     print("test case passed, count is correct")
# else:
#     print("test case failed. count is incorrect")

target_value = "Option 1"

for option in select.options:
    if option.text == target_value:
        option.click()
        print(f" selected option is : {target_value}")
        break
    else:
        print(f"option {target_value} not found")


time.sleep(5)
driver.close()

# how to interact with dropdown
# how to use select class
# how to use different methods
# select by visible text
# select by index
# select by value
# how to count the dropdown values
# loop the dropdown values and if the desired value is found select that value
