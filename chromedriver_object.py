from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Chromedriver_object:
    # Exécution de Chrome driver
    service_obj = Service("D:\\Sauvegarde travaux Cham\\Udemy\\Selenium\\chromedriver_win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
