import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://cnt-ff147476-64c5-4a45-bc1b-2b8250900869.containerhub.tripleten-services.com?lng=pt")

# Faça o aplicativo aguardar 2 segundos para permitir que a página carregue
time.sleep(2)

driver.find_element(By.XPATH, "//button[@aria-pressed='false']").click()

time.sleep(2)

driver.quit()