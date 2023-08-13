#import pytest
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options

#driver: webdriver.Remote

#@pytest.fixture
#def setup_teardown():
    # setup
 #   global driver

  #  chrome_options = Options()
    #chrome_options.add_argument('--headless') # para executar os testes em modo headless basta descomentar esta linha
   # chrome_options.add_argument('--no-sandbox') 
    #chrome_options.binary_location = '/usr/bin/google-chrome'

    #driver = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)

    #driver.get("https://www.saucedemo.com/")
    #driver.maximize_window()
    #driver.implicitly_wait(5)

    # run test
    #yield

    # teardown
    #driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver: webdriver.Remote

@pytest.fixture
def setup_teardown():
    # setup
    global driver
    # para executar local com o chromedriver na pasta bin basta adicionar o caminho do chromedriver na pasta bin
    service = Service(executable_path="chromedriver-linux64/chromedriver")
    webdriver.Chrome(service=service)

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)

    # run test
    yield

    # teardown
    driver.quit()