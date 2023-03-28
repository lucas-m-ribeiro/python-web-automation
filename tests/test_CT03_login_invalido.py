import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login_invalido
class Test_CT03:

    def test_CT03_login_invalido(self):
        msg_esperada = "Epic sadface: Username and password do not match any user in this service"

        #arrange
        login_page = LoginPage()

        # act
        login_page.login("standard_user", "kskskks")

        # assert
        login_page.verify_error_exist()
        login_page.verify_error_message_text(msg_esperada)
