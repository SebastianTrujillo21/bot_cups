from encodings import utf_8
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pandas as pd
from openpyxl import load_workbook
import time

encoding: utf_8
filename = 'Data_Prueba.xlsx'
filesheet = pd.read_excel(filename, usecols='E:H')

workbook = load_workbook(filename)
worksheet = workbook.active

cp = list(filesheet.loc[:, 'CP'])
dir = list(filesheet.loc[:, 'DIRECCION'])
loc = list(filesheet.loc[:, 'LOCALIDAD'])
cp_valor_final = []

for i in range(len(cp)):
    cp_valor_final.append(str(cp[i]).zfill(5))

valor_cup = ""
valor_potenciaP1 = ""
cups = []
potenciasP1 = []

class webScrapping():
    def recolectar_cups_potenciaP1(self):
        for i in range(len(cp)):
            driver.find_element(By.CSS_SELECTOR, "#address").click()
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, "#postalCode").send_keys(cp_valor_final[i])
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
            cups.append(valor_cup)
            valor_potenciaP1 = potenciaP1.text[24:len(potenciaP1.text)]
            potenciasP1.append(valor_potenciaP1)
            driver.refresh()


url = 'https://front-calculator.zapotek.adn.naturgy.com/'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
trabajo = webScrapping()
trabajo.recolectar_cups_potenciaP1()
for index, value in enumerate(cups):
    worksheet.cell(row=index + 2, column=10, value=value)
for index, value in enumerate(potenciasP1):
    worksheet.cell(row=index + 2, column=11, value=value)

workbook.save(filename)
