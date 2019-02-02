from base_test import BaseTest
from page_properties import auth, prod, cart


class Cart(BaseTest):
    def setUp(self):
        BaseTest.setUp(self)

    def tearDown(self):
        BaseTest.tearDown(self)

    def test_verify_cart_contents(self):
        """
        This test will add Sauce Labs Onesie and the Sauce Labs Bike Light
        products to the cart and then verify the items exsist in the cart.
        """
        # Setting some things up for later use.
        products = ["Sauce Labs Onesie", "Sauce Labs Bike Light"]
        p = prod.products # Stores the Product page class in p
        c = cart.cart # Stores the Cart page class in c

        # Log into the site
        auth.login.login()

        # Find and add the specified products to the cart.
        self.assertTrue(p.is_page(), "Not on the products page.")
        p.find_products(products, add_to_cart=True)

        # Navigate to the cart page and verify the selected items are present.
        p.go_to_cart()
        self.assertTrue(c.is_page(), "Not on the cart page.")
        cart_items = c.find_cart_items(products)

        # Verify the correct items are in the cart.
        self.assertTrue(len(products) == len(cart_items), "{} items were found but we expected to find {}.".format(str(len(cart_items)), str(len(products))))
        onesie = False
        light = False
        for item in cart_items:
            name = item.find_element(c.item_name.finder, c.item_name.value)
            if name.is_displayed() and products[0] in name.text:
                onesie = True
            elif name.is_displayed() and products[1] in name.text:
                light = True

        self.assertTrue(onesie and light, "One or both of the products wasn't found. Onesie found: {}, Light found: {}".format(str(onesie), str(light)))
