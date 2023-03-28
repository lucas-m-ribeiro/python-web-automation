import conftest
from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self):
        self.driver = conftest.driver
        self.user_name_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
    
    def fazer_login(self, usuario, senha):
        self.driver.find_element(*self.user_name_field).send_keys(usuario)
        self.driver.find_element(*self.password_field).send_keys(senha)
        self.driver.find_element(*self.login_button).click()