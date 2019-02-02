#####################################################
# This file is for quick access to the page classes #
#####################################################


class LoginPage(object):

    def __init__(self):
        self._login = None

    @property
    def login(self):
        """
        :return:
        :rtype: login_page.Login
        """

        if self._login is None:
            from login_page import Login
            self._login = Login()

        return self._login


class ProductsPage(object):

    def __init__(self):
        self._products = None

    @property
    def products(self):
        """
        :return:
        :rtype: products_page.Products
        """

        if self._products is None:
            from products_page import Products
            self._products = Products()

        return self._products


class CartPage(object):

    def __init__(self):
        self._cart = None

    @property
    def cart(self):
        """
        :return:
        :rtype: cart_page.Cart
        """

        if self._cart is None:
            from cart_page import Cart
            self._cart = Cart()

        return self._cart


auth = LoginPage()
prod = ProductsPage()
cart = CartPage()
