import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
    
driver: webdriver.Remote

@pytest.fixture
def setup_teardown():
    # setup

    service = Service(executable_path="chromedriver.exe")
    webdriver.Chrome(service=service)

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)

    # run test
    yield

    # teardown
    driver.quit()