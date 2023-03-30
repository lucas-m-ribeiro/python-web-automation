import conftest
from selenium.webdriver.common.by import By
from core.selenium import Selenium

class OverviewPage(Selenium):

    def __init__(self):
        self.driver = conftest.driver
        self.product_description = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.finish_button = (By.ID, "finish")

    def verify_product_to_buy(self, item_name):
        item = (self.product_description[0], self.product_description[1].format(item_name))
        self.verify_elements_exists(item)

    def click_finish_button(self):
        self.click(self.finish_button)