from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Exécution de Chrome driver
service_obj = Service("D:\\Sauvegarde travaux Cham\\Udemy\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# print(len(checkboxes))
#
# for checkbox in checkboxes:
#     if checkbox.get_attribute("value").__eq__("option2"):
#         checkbox.click()
#         assert checkbox.is_selected()
name = "Cham"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()
