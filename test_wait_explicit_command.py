import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

browser = webdriver.Chrome()

browser.maximize_window()

browser.get("https://chercher.tech/pratice/explicit-wait-sample-selenium-webdriver")
wait = WebDriverWait(browser, 30)

# alert is present
browser.find_element(By.ID, "alert").click()
wait.until(Ec.alert_is_present())
time.sleep(2)

#text to be present in element
browser.find_element(By.ID, "populate-text").click()
wait.until(Ec.text_to_be_present_in_element((By.XPATH, "//*[@class=target-text]"), "Selenium Webdriver"))
target_text = browser.find_element(By.XPATH, "//*[@class=target-text]").text
assert target_text == "Selenium Webdriver"
time.sleep(2)

#element_to_be_clickable
browser.find_element(By.ID, "display-other-button").click()
wait.until(Ec.element_to_be_clickable((By.ID, "hidden")))
time.sleep(2)

#element_to_be_selected
checkbox = browser.find_element(By.ID, "ch")
browser.find_element(By.ID, "checkbox-").click()
wait.until(Ec.element_to_be_selected(checkbox))
time.sleep(2)
