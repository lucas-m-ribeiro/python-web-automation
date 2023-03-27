from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import conftest
import pytest

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class Test_CT02:

    def test_CT02_login_valido(self):

        driver = conftest.driver

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()