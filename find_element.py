import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
# Substitua nosso link pelo link do seu próprio servidor aqui
driver.get("https://cnt-922f28fd-f378-4702-871d-1e8792c7b1f8.containerhub.tripleten-services.com?lng=pt")

# Pause a execução por 2 segundos para permitir que a página carregue por completo
time.sleep(2)

# Encontre o elemento de logotipo usando seu seletor de CSS
element = driver.find_element(By.CSS_SELECTOR, "img.logo-image")

# Imprima o elemento encontrado no console
print(element)

# Feche o navegador e encerre a sessão do WebDriver
driver.quit()