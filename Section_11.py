from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Exécution de Chrome driver
service_obj = Service("D:\\Sauvegarde travaux Cham\\Udemy\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
# Fenêtre en plein écran driver.fullscreen_window()
# Cibler des éléments HTML sur la page visitée
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Mon nom...")
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
print(driver.find_element(By.ID, "exampleInputPassword1").get_attribute("type"))
driver.find_element(By.ID, "exampleCheck1").click()

# Static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
# sélectioner par texte : dropdown.select_by_visible_text("Female")
# sélectionner par l'attribut HTML "value" : dropdown.select_by_value()

# XPATH
driver.find_element(By.XPATH, "//input[@type='submit']").click()
success_message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(success_message)
assert "success" in success_message  # insensible à la casse

