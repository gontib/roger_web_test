import time
from selenium.webdriver.common.by import By
from base_page import BasePage, Locator


class Cart(BasePage):
    """
        Locators and methods for the cart page.
    """

    def __init__(self):
        super(Cart, self).__init__()

        self.cart_item_parents = Locator(By.CLASS_NAME, "cart_item")
        self.item_name = Locator(By.CLASS_NAME, "inventory_item_name")

    def is_page(self):
        """
            Determines if we are on the products page.
        :return: bool
        """
        # Adding the sleep so you can see the page load
        time.sleep(1)
        return "cart.html" in self.get_page_url()

    def find_cart_items(self, product_name):
        """
            Finds the parent elements of the specified items.
        :param product_name: str - name(s) of item to be found.
        :return:
        """
        parent_elements = self.cart_item_parents.get_elements()

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

        return el_list
