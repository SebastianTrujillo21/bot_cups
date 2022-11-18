from encodings import utf_8
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

#############################################

encoding: utf_8

url = 'https://front-calculator.zapotek.adn.naturgy.com/'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

# acciones
driver.find_element(By.CSS_SELECTOR, "#address").click()
time.sleep(2)


################## insertar ###########################

codigo_postal = "32005"
valor_calle = "DO PROGRESO 2 1"
localidad = "OURENSE"

driver.find_element(By.CSS_SELECTOR, "#postalCode").send_keys(codigo_postal)
time.sleep(2)
city = driver.find_element(By.CSS_SELECTOR, "#city")
selector_city = Select(city)
selector_city.select_by_visible_text(localidad)
calle = driver.find_element(By.CSS_SELECTOR, "#street")
calle.click()
calle.send_keys(valor_calle)
time.sleep(5)
calle.send_keys(Keys.DOWN)
calle.send_keys(Keys.ENTER)
driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
time.sleep(5)

#FUNCION PARA REFRESCAR LA PAGINA Y HACERLO TO DO DE NUEVO (TODO IMPLEMENTARLO)
#driver.refresh()
#time.sleep(10)



#TODO CREAR UNA CLASE O FUNCION PARA PODER AÑADIR TODA LA LOGICA DEL SCRAPING Y PASAR POR PARAMETRO LA VARIABLE Y HACEMOS UN FOR DE LAS VARIABLES QUE TENEMOS