import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class Test_CT02:

    def test_CT02_login_valido(self):
        # Arrange
        login_page = LoginPage()
        page = HomePage()

        # Act
        login_page.login("standard_user", "secret_sauce")
        
        # Assert
        page.verify_sucessfuly_login