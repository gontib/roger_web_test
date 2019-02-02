from base_test import BaseTest


class BasePage(object):
    """
        All page classes will inherit from this class.
    """

    def __init__(self):
        self.driver = BaseTest.get_driver()

    def is_page(self):
        raise Exception("The is_page method needs to be extended in the page class.")

    def get_page_url(self):
        return self.driver.current_url


class Locator(object):
    """
        This class object will store locator and element information.
    """

    driver = None

    def __init__(self, finder, value):

        self.driver = BaseTest.get_driver()
        self.finder = finder
        self.value = value
        self.element = None
        self.elements = []

    def get_element(self):
        self.element = self.driver.find_element(self.finder, self.value)
        return self.element

    def get_elements(self):
        self.elements = self.driver.find_elements(self.finder, self.value)
        return self.elements
