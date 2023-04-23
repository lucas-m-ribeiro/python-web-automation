import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

driver: webdriver.Remote

@pytest.fixture
def setup_teardown():
    # setup
    global driver

    chrome_options = Options()
    chrome_options.binary_location = '/usr/bin/google-chrome-stable'

    #service = Service(executable_path="chromedriver")
    drive = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)

    # run test
    yield

    # teardown
    driver.quit()