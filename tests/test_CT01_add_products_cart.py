from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import conftest
import pytest

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.add_product
class TestCT01:

    def test_CT01_Add_products_cart(self):

        driver = conftest.driver
        
        #fazendo login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        #adicionando primeiro produto no carrinho
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click()
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed(), "Primeiro produto adicionado com sucesso"

        #adicionando segundo produto no carrinho
        driver.find_element(By.ID, "continue-shopping").click()
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").click()
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

        #verificando os dois produtos no carrinho
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed(), "Primeiro produto adicionado com sucesso"
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed(), "Segundo produto adicionado com sucesso"
