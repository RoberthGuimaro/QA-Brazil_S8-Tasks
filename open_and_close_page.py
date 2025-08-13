from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# Abra a página inicial do Urban Routes
driver.get("https://cnt-8db15071-c316-4ba6-8819-ff8a96a61427.containerhub.tripleten-services.com?lng=pt")

# Verifique se a URL contém tripleten-services.com
assert "tripleten-services" in driver.current_url

# Feche o navegador
driver.quit()
