import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    """
        All test classes will inherit from this class.
    """

    driver = None

    def setUp(self):
        self.driver = self.get_driver()
        self.driver.get("https://www.saucedemo.com/")

    def tearDown(self):
        self.driver.close()

    @staticmethod
    def get_driver():
        if BaseTest.driver is None:
            BaseTest.driver = webdriver.Chrome()

        return BaseTest.driver
