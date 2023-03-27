
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pytest
import conftest

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class Test_CT03:

    def test_CT03_login_invalido(self):

        driver = conftest.driver

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret")
        driver.find_element(By.ID, "login-button").click()
        message = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        assert message.text == "Epic sadface: Username and password do not match any user in this service"
        assert len(driver.find_elements(By.XPATH, "//span[@class='title']")) == 0
