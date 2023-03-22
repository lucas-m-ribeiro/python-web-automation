from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://www.saucedemo.com/")

#findElement()
username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
btn_login = browser.find_element(By.ID, "login-button")

#sendKeys
username.send_keys("standard_user")
password.send_keys("secret_sauce")

#click()
btn_login.click()

#text
product_title = browser.find_element(By.XPATH, "//span[@class='title']")
print(product_title.text)
assert product_title.text == "Products"

#GETATTRIBUTE
img_backpack = browser.find_element(By.XPATH, "(//img[@class='inventory_item_img'])[1]")
print(img_backpack.get_attribute("alt"))
assert img_backpack.get_attribute("alt") == "Sauce Labs Backpack"