import time

from selenium.webdriver.common.by import By
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
# Abra uma nova instância do Chrome WebDriver
driver = webdriver.Chrome()

# Abra a URL especificada no navegador
driver.get("https://cnt-67b991a3-3ecb-440b-bf82-042bf9cb1878.containerhub.tripleten-services.com?lng=pt")

# Pause a execução por 2 segundos para permitir que a página carregue por completo
time.sleep(2)

# Encontre o elemento de título usando seu seletor de CSS
element = driver.find_element(By.CSS_SELECTOR, ".logo-disclaimer")

print(element)
# Feche o navegador e encerre a sessão do WebDriver
driver.quit()
