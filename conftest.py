import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver: webdriver.Remote

@pytest.fixture
def setup_teardown():

    global driver

    SUT = 'https://www.saucedemo.com/'
    SERVER = 'http://localhost:4445'

    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox') 
    chrome_options.set_capability('browserVersion', '145.0')
    chrome_options.set_capability('platformName', 'linux')
    #chrome_options.add_argument('--headless') # para executar os testes em modo headless basta descomentar esta linha

    driver = webdriver.Remote(command_executor=SERVER, options=chrome_options)

    driver.get(SUT)
    driver.maximize_window()
    driver.implicitly_wait(5)

    # run test
    yield

    # teardown
    driver.quit()