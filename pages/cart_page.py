import conftest
from selenium.webdriver.common.by import By
from core.selenium import Selenium

class CartPage(Selenium):

    def __init__(self):
        self.driver = conftest.driver
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.button_continue_shopping = (By.ID, "continue-shopping")
        self. button_checkout = (By.ID, "checkout")

    def verify_product_in_cart(self, item_name):
        item = (self.item_inventario[0], self.item_inventario[1].format(item_name))
        self.verify_elements_exists(item)

    def click_button_continue_shopping(self):
        self.click(self.button_continue_shopping)

    def click_checkout_button(self):
        self.click(self.button_checkout)