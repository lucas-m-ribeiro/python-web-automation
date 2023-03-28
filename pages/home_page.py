from pages.base_page import BasePage
import conftest
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.page_title = (By.XPATH, "//span[@class='title']")
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.button_add_cart = (By.XPATH, "//*[text()='Add to cart']")
        self.cart_icon = (By.XPATH, "//*[@class='shopping_cart_link']")

    def verify_sucessfuly_login(self):
        self.verify_elements_exists(self.page_title)

    def add_in_cart(self, item_name):
        item = (self.item_inventario[0], self.item_inventario[1].format(item_name))
        self.click(item)
        self.click(self.button_add_cart)

    def acess_cart(self):
        self.click(self.cart_icon)