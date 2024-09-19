from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.maximize_window()
website = "https://the-internet.herokuapp.com/nested_frames"
driver.get(website)

# switch to top frame

driver.switch_to.frame("frame-top")

# switch to left frame

# driver.switch_to.frame("frame-left")
# content = driver.find_elements(By.TAG_NAME, value="body")[0].text

# switch to middle frame


driver.switch_to.frame("frame-middle")

content = driver.find_element(By.ID, value="content").text

print("content in middle frame : ", content)

time.sleep(5)

# switch to default content
driver.switch_to.default_content()

# switch to bottom frame

driver.switch_to.frame("frame-bottom")
content_bottom = driver.find_element(By.TAG_NAME, value="body").text
print("content in bottom frame : ", content_bottom)


time.sleep(5)
driver.close()
