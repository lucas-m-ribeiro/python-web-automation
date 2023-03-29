import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_information_page import CheckoutInformation
from pages.overiew_page import OverviewPage
from pages.finish_order_page import FinishOrderPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.buy_one_product
class Test_CT04_buy_one_produt:

    def test_CT04_buy_one_product(self):

        # ARRANGE

        produto_1 = "Sauce Labs Backpack"
        message = "Thank you for your order!"

        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()
        ck_information = CheckoutInformation()
        overview_page = OverviewPage()
        finish_order_page = FinishOrderPage()

        login_page.login("standard_user", "secret_sauce")

        # ACTION

        # adicionando primeiro produto no carrinho
        home_page.add_in_cart(produto_1)
        home_page.acess_cart()
        cart_page.verify_product_in_cart(produto_1)

        #clicando no botao checkout
        cart_page.click_checkout_button()

        #Preencehendo com meus dados
        ck_information.fill_in_first_name("Lucas")
        ck_information.fill_in_last_name("Monteiro Ribeiro")
        ck_information.fill_in_postal_code("40028922")
        ck_information.click_continue_button()

        #confirm the product
        overview_page.verify_product_to_buy("Sauce Labs Backpack")
        overview_page.click_finish_button()

        # ASSERTIONS

        #cofirm the order
        finish_order_page.verify_order()
        finish_order_page.verify_messge_order(message)
