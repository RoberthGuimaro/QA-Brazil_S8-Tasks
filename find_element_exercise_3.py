import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
# Abra uma nova instância do Chrome WebDriver
driver = webdriver.Chrome()

# Abra a URL especificada no navegador
driver.get("https://cnt-5c9834f3-f205-43d3-9dab-513f916cad8f.containerhub.tripleten-services.com?lng=pt")

# Pause a execução por 2 segundos para permitir que a página carregue por completo
time.sleep(2)

# Encontre o campo de entrada DE e o campo de entrada PARA usando seus IDs
from_field = driver.find_element(By.ID, "from")
to_field = driver.find_element(By.ID,"to")

placeholder_from_text = from_field.get_attribute("placeholder")
placeholder_to_text = to_field.get_attribute("placeholder")

# Teste o atributo placeholder de cada campo de entrada para garantir que eles estejam exibindo o texto correto
assert placeholder_from_text == "East 2nd Street, 601", f"O placeholder 'from' não contém o conteúdo correto"
assert placeholder_to_text == "1300 1st St", f"O placeholder 'to' não contém o conteúdo correto"

print(f"Os placeholders estão corretos")

# Feche o navegador e encerre a sessão do WebDriver
driver.quit()
