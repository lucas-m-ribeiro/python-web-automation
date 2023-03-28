import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class Test_CT03:

    def test_CT03_login_invalido(self):
        #arrange
        login_page = LoginPage()

        # act
        login_page.login("standard_user", "kskskks")

        # assert
        login_page.verify_error_message()

        # assertion deprectaed
        
        # assert message.text == "Epic sadface: Username and password do not match any user in this service"
        # assert len(driver.find_elements(By.XPATH, "//span[@class='title']")) == 0
