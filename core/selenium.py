import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys

class Selenium:

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
    
    def wait_visible_el(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(*locator))
    
    def verify_element_not_exists(self, element):
        assert len(self.find_element(element)) == 0, f"O elemento '{element}' foi encontrado na tela, é esperado que ele não exista!"

    def double_click(self, locator):
        element = self.wait_visible_el(locator)
        ActionChains(self.driver).double_click(element).perform()
    
    def click_right_button(self, locator):
        element = self.wait_visible_el(locator)
        ActionChains(self.driver).context_click(element).perform()

    def press_key(self, locator, key):
        element = self.find_element(locator)
        if key == "ENTER":
            element.send_keys(Keys.ENTER)
        elif key == "SPACE":
            element.send_keys(Keys.SPACE)
        elif key == "F1":
            element.send_keys(Keys.F1)
