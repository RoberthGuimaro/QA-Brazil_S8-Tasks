import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.by import By
from selenium import webdriver

# Abra uma nova instância do Chrome WebDriver
driver = webdriver.Chrome()

# Abra a URL especificada no navegador
driver.get("https://cnt-b530c3ef-700f-45d7-833c-e91397fc424e.containerhub.tripleten-services.com?lng=pt")

# Pause a execução por 2 segundos para permitir que a página carregue por completo
time.sleep(20)

# Encontre todos os elementos na página usando um seletor de XPath
elements = driver.find_elements(By.XPATH, "//div[@class='dst-picker-marker']")

print(len(elements))

# Verifique se o número de elementos encontrados é maior que 1 usando len()
assert len(elements)>0

# Feche o navegador e encerre a sessão do WebDriver
driver.quit()

