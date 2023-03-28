from selenium.webdriver.common.by import By
import pytest
import conftest

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.buy_one_product
class Test_CT04_buy_one_produt:

    def test_CT04_buy_one_product(self):

        driver = conftest.driver

        #fazendo login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()


        #adicionando primeiro produto no carrinho
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click()
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()

        #clicando no botao checkout
        driver.find_element(By.ID, "checkout").click()

        #Preencehendo com meus dados
        driver.find_element(By.ID, "first-name").send_keys("Lucas")
        driver.find_element(By.ID, "last-name").send_keys("Monteiro Ribeiro")
        driver.find_element(By.ID, "postal-code").send_keys("4568214569")
        driver.find_element(By.ID, "continue").click()

        #confirm the product
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
        driver.find_element(By.ID, "finish").click()

        #cofirm the order

        order_buy = driver.find_element(By.XPATH, "//h2[@class='complete-header']")

        assert order_buy.text == "Thank you for your order!", "Compra não foi finalizada com sucesso!"

