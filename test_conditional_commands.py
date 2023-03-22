import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://demo.applitools.com/")

username = browser.find_element(By.ID, "username")
checkbox_remeber_me = browser.find_element(By.XPATH, "//*[@type='checkbox']")

#isDisplayed
print(username.is_displayed())
assert username.is_displayed()

#is enable
print(username.is_enabled())
assert username.is_enabled()

# is_select
print(checkbox_remeber_me.is_selected())
assert not checkbox_remeber_me.is_selected()

#clicando no elemento
checkbox_remeber_me.click()

assert checkbox_remeber_me.is_selected()

