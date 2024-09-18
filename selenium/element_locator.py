import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestSelenium(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test(self):
        self.driver.get("https://www.selenium.dev/")
        searchbar = self.driver.find_element(by=By.ID, value="Layer_1")
        print(searchbar.parent)
        # self.driver.find_element(by=By.XPATH, value=("#APjFqb")) # ini hanya code tidak terkait dari tutorial video youtube

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
