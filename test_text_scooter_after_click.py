import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urban_routes_main_page import UrbanRoutesPage


def test_personal_scooter_option():
    # Etapa 1: Abra o aplicativo e atualize a URL após iniciar o servidor
    driver = webdriver.Chrome()
    driver.get("https://cnt-c8c7ec5f-6fd3-4b37-9956-8edf2f736256.containerhub.tripleten-services.com?lng=pt")

    # Crie uma instância da classe de página
    urban_routes_page = UrbanRoutesPage(driver)

    # Adicione uma espera explícita para o campo "De"
    wait = WebDriverWait(driver, 10)  # Define um tempo máximo de 10 segundos
    wait.until(EC.presence_of_element_located(urban_routes_page.FROM_LOCATOR))

    # Etapa 3: use métodos POM para executar ações na página
    # Insira os locais "De" e "Para"
    urban_routes_page.enter_from_location('East 2nd Street, 601')
    urban_routes_page.enter_to_location('1300 1st St')

    # Selecione a opção "Personal"
    urban_routes_page.click_personal_option()
    time.sleep(2)

    # Clique no ícone "Scooter"
    urban_routes_page.click_scooter_icon()
    time.sleep(2)

    # Etapa 4: Verifique se o texto Scooter é exibido corretamente
    actual_value = urban_routes_page.get_scooter_text()
    expected_value = "Scooter"
    assert expected_value in actual_value, f"Esperado '{expected_value}', mas obtido '{actual_value}'"

    # Feche o navegador
    driver.quit()