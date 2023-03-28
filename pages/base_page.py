import conftest

class BasePage:

    def __init__(self):
        self.driver = conftest.driver


    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def click(self, locator):
        self.find_element(locator).click()

    def verify_elements_exists(self, locator):
        assert self.find_element(locator).is_displayed(), f"O elemento '{locator}' não foi encontrado na tela!"

    def get_text_element(self, locator):
        return self.find_element(locator).text