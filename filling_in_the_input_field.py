import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://cnt-18acffdd-5ea5-46ca-acfa-f262aa43066f.containerhub.tripleten-services.com?lng=pt")

# Pause a execução por 2 segundos para permitir que a página carregue por completo
time.sleep(2)

# Encontre o campo DE e o preencha
driver.find_element(By.ID, "from").send_keys("East 2nd Street, 601")

# Encontre o campo PARA e o preencha
driver.find_element(By.ID, "to").send_keys("1300 1st St")

time.sleep(2)

# Encontre o botão "Chamar um táxi" e clique nele
driver.find_element(By.XPATH, "//button[@class='button round']").click()

# Adicione uma espera explícita para que o campo carregue
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.ID,"comment")))

# Escreva um comentário para o motorista
driver.find_element(By.ID, "comment").send_keys("Oi amigo")

time.sleep(2)

print(driver.find_element(By.ID, "comment").get_attribute("value"))

# Verifique se o seu comentário é o esperado
assert driver.find_element(By.ID, "comment").get_attribute("value") == "Oi amigo"

driver.quit()
