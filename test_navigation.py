from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="chromedriver.exe")
webdriver.Chrome(service=service)

browser = webdriver.Chrome()

browser.get('https://google.com')

# Comandos para navegação do selenium

#maximize
browser.maximize_window()

#refresh
browser.refresh()
time.sleep(3)

#back
browser.get('https://youtube.com')
time.sleep(2)

browser.back()

#foward
browser.forward()
time.sleep(3)

# close
browser.switch_to.new_window("tab")
time.sleep(3)

browser.close()
time.sleep(3)

#quit
browser.quit()

# o metodo close fecha a janela aberta no momento da execução
# comando quit encerra todo processo de execução do teste automatizado