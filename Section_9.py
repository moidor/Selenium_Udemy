from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Exécution de Chrome driver
service_obj = Service("D:\\Sauvegarde travaux Cham\\Udemy\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# Exécution de geckodriver pour Firefox
# service_obj = Service("D:\\Sauvegarde travaux Cham\\Udemy\\Selenium\\geckodriver_win64\\geckodriver.exe")
# driver = webdriver.Firefox(service=service_obj)

# Exécution de Microsoft Edge WebDriver
# service_obj = Service("D:\\Sauvegarde travaux Cham\\Udemy\\Selenium\\edgedriver_win64\\msedgedriver.exe")
# driver = webdriver.Edge(service=service_obj)

driver.maximize_window()  # agrandir la fenêtre contrairement à .minimize_window() qui réduit
driver.get("http://google.com")  # se rendre à cette url
# driver.get("https://rahulshettyacademy.com")
print(driver.title)  # afficher le titre de l'onglet
print(driver.current_url)  # afficher l'url actuelle
driver.get("http://eurosport.fr")
driver.back()  # revenir à la page précédente
driver.refresh()  # rafraîchir la page
driver.forward()  # afficher la page suivante
# driver.close()
