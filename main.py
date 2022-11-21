from encodings import utf_8
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pandas as pd
import time

encoding: utf_8
filesheet = pd.read_excel('Data_Prueba.xlsx')
print(filesheet)
codigo_postal = "32005"
valor_calle = "DO PROGRESO 2 1"
localidad = "OURENSE"
valor_cup = ""
valor_potenciaP1 = ""


class webScrapping():
    def recolectar_cups_potenciaP1(self):
        for i in range(10):
            driver.find_element(By.CSS_SELECTOR, "#address").click()
            time.sleep(2)
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
            cup = driver.find_element(By.XPATH,
                                      "//body/div[@id='root']/section[@role='main']/div/div/div/div/div[2]/p[1]")
            potenciaP1 = driver.find_element(By.XPATH, "//p[3]")

            valor_cup = cup.text[6:len(cup.text)]
            valor_potenciaP1 = potenciaP1.text[24:len(potenciaP1.text)]

            print(valor_cup)
            print(valor_potenciaP1)
            driver.refresh()


url = 'https://front-calculator.zapotek.adn.naturgy.com/'
#driver = webdriver.Chrome()
#driver.maximize_window()
#driver.get(url)
#trabajo = webScrapping()
#trabajo.recolectar_cups_potenciaP1()
