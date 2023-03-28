from pages.base_page import BasePage
import conftest
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.page_title = (By.XPATH, "//span[@class='title']")


    def verify_sucessfuly_login(self):
        self.verify_elements_exists(self.page_title)
