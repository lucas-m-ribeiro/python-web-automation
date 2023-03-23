from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="chromedriver.exe")
webdriver.Chrome(service=service)

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.implicitly_wait(5)

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
