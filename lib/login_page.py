from selenium.webdriver.common.by import By
from base_page import BasePage, Locator


class Login(BasePage):
    """
        Locators and methods for the login page.
    """

    def __init__(self):
        super(Login, self).__init__()

        self.fld_username = Locator(By.ID, "user-name")
        self.fld_password = Locator(By.ID, "password")
        self.btn_submit = Locator(By.CLASS_NAME, "login-button")

    def is_page(self):
        """
            Determines if we are on the login page.
        :return: bool
        """
        return self.get_page_url() == "https://www.saucedemo.com/" and self.fld_username.get_element().is_displayed()

    def login(self, username="standard_user", password="secret_sauce"):
        if not self.is_page():
            raise Exception("Not the one login page.")

        self.fld_username.get_element().send_keys(username)
        self.fld_password.get_element().send_keys(password)
        self.btn_submit.get_element().click()

