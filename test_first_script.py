from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="chromedriver.exe")
webdriver.Chrome(service=service)

browser = webdriver.Chrome()

browser.get('https://google.com')
time.sleep(5)
