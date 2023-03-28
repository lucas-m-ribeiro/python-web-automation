from selenium.webdriver.common.by import By
import conftest
import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class Test_CT02:

    def test_CT02_login_valido(self):
        # arrange
        driver = conftest.driver
        login_page = LoginPage()

        # act
        login_page.fazer_login("standard_user", "secret_sauce")
        
        # Assert
        assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()