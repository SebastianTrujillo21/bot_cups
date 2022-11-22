from encodings import utf_8
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pandas as pd
import time

encoding: utf_8
filesheet = pd.read_excel('100_datos_prueba.xlsx', usecols='E:H')

cp = list(filesheet.loc[:, 'CP'].zfill(2))
dir = list(filesheet.loc[:, 'DIRECCION'])
loc = list(filesheet.loc[:, 'LOCALIDAD'])
print(cp)

valor_cup = ""
valor_potenciaP1 = ""

datas = {"cups": [],
         "potencia": []}


class webScrapping():
    def recolectar_cups_potenciaP1(self):
        for i in range(20):
            driver.find_element(By.CSS_SELECTOR, "#address").click()
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, "#postalCode").send_keys(cp[i])
            time.sleep(2)
            city = driver.find_element(By.CSS_SELECTOR, "#city")
            selector_city = Select(city)
            selector_city.select_by_visible_text(loc[i])
            calle = driver.find_element(By.CSS_SELECTOR, "#street")
            calle.click()
            calle.send_keys(dir[i])
            time.sleep(5)
            calle.send_keys(Keys.DOWN)
            calle.send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
            time.sleep(6)
            cup = driver.find_element(By.XPATH,
                                      "//body/div[@id='root']/section[@role='main']/div/div/div/div/div[2]/p[1]")
            potenciaP1 = driver.find_element(By.XPATH, "//p[3]")

            valor_cup = cup.text[6:len(cup.text)]
            datas["cups"].append(valor_cup)
            valor_potenciaP1 = potenciaP1.text[24:len(potenciaP1.text)]
            datas["potencia"].append(valor_potenciaP1)

            print(valor_cup)
            print(valor_potenciaP1)
            driver.refresh()


url = 'https://front-calculator.zapotek.adn.naturgy.com/'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
trabajo = webScrapping()
trabajo.recolectar_cups_potenciaP1()
print(datas)
df = pd.DataFrame(datas)
with pd.ExcelWriter('100_datos_prueba.xlsx', mode='a') as writer:
    df.to_excel(writer, sheet_name='Hoja2')
