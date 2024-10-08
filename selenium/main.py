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
        self.driver.get("https://www.google.com/")
        searchbar = self.driver.find_element(by=By.NAME, value="q")
        searchbar.send_keys("indonesia")
        searchbar.send_keys(Keys.RETURN)
        time.sleep(2)
        resault = self.driver.find_element(by=By.ID, value="gsr")
        print(resault.text, "test\n")
        assert ("Link Footer") in resault.text
        # self.assertIn("Google", self.driver.title)
        # breakpoint()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
