import time
from selenium.webdriver.common.by import By
from base_page import BasePage, Locator


class Products(BasePage):
    """
        Locators and methods for the products page.
    """

    def __init__(self):
        super(Products, self).__init__()

        self.inv_parents = Locator(By.CLASS_NAME, "inventory_item")
        self.item_name = Locator(By.CLASS_NAME, "inventory_item_name")
        self.btn_add_to_cart = Locator(By.CLASS_NAME, "add-to-cart-button")
        self.btn_shopping_cart = Locator(By.XPATH, "//*[@id='shopping_cart_container']/a")

    def is_page(self):
        """
            Determines if we are on the products page.
        :return: bool
        """
        return "inventory.html" in self.get_page_url()

    def find_products(self, product_name, add_to_cart=False):
        """
            Finds the parent elements of the specified items.
        :param product_name: str - name(s) of item to be found.
        :param add_to_cart: bool - Will add the found items to the cart if True
        :return:
        """
        parent_elements = self.inv_parents.get_elements()

        el_list = []
        if isinstance(product_name, str):
            for element in parent_elements:
                item = element.find_element(self.item_name.finder, self.item_name.value)
                if product_name in item.text:
                    el_list.append(element)

        elif isinstance(product_name, list):
            for element in parent_elements:
                item = element.find_element(self.item_name.finder, self.item_name.value)
                for p in product_name:
                    if p in item.text:
                        el_list.append(element)
                if len(product_name) == len(el_list):
                    break

        if add_to_cart:
            self.add_items_to_cart(el_list)
        else:
            return el_list

    def add_items_to_cart(self, elements):
        """
            Will click the Add to Cart button
        :param elements: List of WebElement objects
        :return:
        """
        for element in elements:
            add_button = element.find_element(self.btn_add_to_cart.finder, self.btn_add_to_cart.value)
            add_button.click()
            # I added the sleep because it was somehow adding a third product when going full speed.
            time.sleep(.5)

    def go_to_cart(self):
        """
            Clicks the cart button to navigate to the cart page.
        """
        self.btn_shopping_cart.get_element()
        self.btn_shopping_cart.element.click()
