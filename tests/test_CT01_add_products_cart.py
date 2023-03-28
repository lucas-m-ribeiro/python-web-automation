import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
import time
@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.add_product
class TestCT01:

    def test_CT01_Add_products_cart(self):

        produto_1 = "Sauce Labs Backpack"
        produto_2 = "Sauce Labs Bike Light"
        
        #Arrane
        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()
        login_page.login("standard_user", "secret_sauce")

        # ACT
        # adicionando primeiro produto no carrinho
        home_page.add_in_cart(produto_1)
        home_page.acess_cart()
        cart_page.verify_product_in_cart(produto_1)

        # #adicionando segundo produto no carrinho
        cart_page.click_button_continue_shopping()
        home_page.add_in_cart(produto_2)
        home_page.acess_cart()

        # Assert
        cart_page.verify_product_in_cart(produto_1)
        cart_page.verify_product_in_cart(produto_2)