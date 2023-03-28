import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.user_name_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message_login = (By.XPATH, "//*[@data-test='error']")

    def login(self, usuario, senha):
        self.send_keys(self.user_name_field, usuario)
        self.send_keys(self.password_field, senha)
        self.click(self.login_button)  

    def verify_error_message(self):
        self.verify_elements_exists(self.error_message_login)