from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://www.saucedemo.com/")

#findElement()
username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")

#sendkeys
username.send_keys("standard_user")
password.send_keys("secret_sauce")


time.sleep(5)

browser.quit()

#find elements - A diferença é que este comando traz mais de um elemento.
#para rodar cada exemplo deixe um comentado.

auth_field = browser.find_elements(By.XPATH, "//*[@class='input_error form_input']")
print(auth_field)
print(len(auth_field))
assert len(auth_field) == 3, "O numero de elementos não é igual ao esperado"
