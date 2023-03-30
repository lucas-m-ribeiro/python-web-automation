import conftest
from selenium.webdriver.common.by import By
from core.selenium import Selenium

class LoginPage(Selenium):

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

    def verify_error_exist(self):
        self.verify_elements_exists(self.error_message_login)

    def verify_error_message_text(self, text_esperado):
        texto_encontrado = self.get_text_element(self.error_message_login)
        assert texto_encontrado == text_esperado, f"O texto retornado foi: '{texto_encontrado}', mas era esperado o texto '{text_esperado}'"