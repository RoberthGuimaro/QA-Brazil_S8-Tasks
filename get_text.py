import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://cnt-59dbee69-88e7-487e-b1c6-4a0ba786b324.containerhub.tripleten-services.com?lng=pt")

# Pause a execução por 2 segundos para permitir que a página carregue por completo
time.sleep(2)

# Encontre o campo DE e o preencha
driver.find_element(By.ID, "from").send_keys("East 2nd Street, 601")

# Encontre o campo PARA e o preencha
driver.find_element(By.ID, "to").send_keys("1300 1st St")

time.sleep(2)

# Obtenha o texto do modo "Fastest"
mode = driver.find_element(By.XPATH, "//div[@class='mode active']").text

print(mode)

time.sleep(2)

# Faça um assert para verificar se o texto da variável mode é "Fastest"
assert mode == "Flash"

driver.quit()