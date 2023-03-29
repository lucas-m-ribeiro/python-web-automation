import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FinishOrderPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.order_buy = (By.XPATH, "//h2[@class='complete-header']")
        self.message_order = (By.XPATH, "//*[@id='checkout_complete_container']/h2")

    def verify_order(self):
        self.verify_elements_exists(self.order_buy)

    def verify_messge_order(self, texto_esperado):
        texto_encontrado = self.get_text_element(self.message_order)
        assert texto_encontrado == texto_esperado, f"O texto retornado foi: '{texto_encontrado}', mas era esperado o texto '{texto_esperado}'"
