import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutInformation(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.button_continue = (By.ID, "continue")

    def fill_in_first_name(self, name):
        self.send_keys(self.first_name_field, name)

    def fill_in_last_name(self, last_name):
        self.send_keys(self.last_name_field, last_name)
            
    def fill_in_postal_code(self, code_number):
        self.send_keys(self.postal_code_field, code_number)

    def click_continue_button(self):
        self.click(self.button_continue)
        
