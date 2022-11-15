# -*- coding: utf -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import bs4
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.chrome.service import Service
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import auth_data

url="http://www.k-chermet.ru/index.php?option=com_content&view=article&id=45&Itemid=63"
options=webdriver.ChromeOptions()
options.add_argument('--start-maximized')

# options.add_argument("--headless")

options.add_argument("")

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)

def auth():
    driver.get(url)
    input_login = driver.find_element(By.XPATH,
                                      "/html/body/div/div[3]/div/div/div[1]/div/div/div/div/div/div/form/p/input[1]")
    input_login.send_keys(auth_data.login_data)

    input_password = driver.find_element(By.XPATH,
                                         "/html/body/div/div[3]/div/div/div[1]/div/div/div/div/div/div/form/p/input[2]")
    input_password.send_keys(auth_data.password_data)
    input_password.send_keys(Keys.RETURN)


def clicker_to_list():
    driver.find_element(By.XPATH, '/html/body/table/tbody/tr[4]/td/table/tbody/tr/td[1]/table/tbody/tr/td[7]/a').click()

    driver.find_element(By.XPATH,
                        '/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr/td/table/tbody/tr[3]/td[1]/a').click()

    driver.find_element(By.XPATH,
                        '/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[2]/td/table[1]/tbody/tr[4]/td/a').click()

    driver.find_element(By.XPATH,
                        '/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[2]/td/table[1]/tbody/tr/td[1]/table/tbody/tr[1]/td/a').click()

    driver.find_element(By.XPATH,
                        '/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/select/option[2]').click()

    driver.find_element(By.XPATH,
                        "/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[4]/td/table[1]/tbody/tr[3]/td[2]/input[1]").clear()
    input_count_list_display = driver.find_element(By.XPATH,
                                                   "/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[4]/td/table[1]/tbody/tr[3]/td[2]/input[1]")
    input_count_list_display.send_keys("60")
    driver.find_element(By.XPATH,
                        '/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[4]/td/table[1]/tbody/tr[3]/td[2]/input[2]').click()  ## показать

def clicks_for_metal_combine():
    for i in range(3,15):
        unelected=[5,11,12]
        if i not in unelected:
            element=f"/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[4]/td/table[2]/tbody/tr[{str(i)}]/td[6]/input"
            driver.find_element(By.XPATH, element).click()

    driver.find_element(By.XPATH, "/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[4]/td/table[2]/tbody/tr[16]/td[2]/input[1]").click()

def clicks_for_metal_plant():
    driver.find_element(By.XPATH,
                        "/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[4]/td/table[1]/tbody/tr[1]/td[2]/select/option[3]").click()  # отрасль предприятия - металлургический завод
    driver.find_element(By.XPATH,
                        '/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[4]/td/table[1]/tbody/tr[3]/td[2]/input[2]').click()  # показать

    for i in range(3, 61):
        selected = [4, 6, 10, 13, 19, 22, 46]
        if i in selected:
            element = f"/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[4]/td/table[2]/tbody/tr[{str(i)}]/td[6]/input"
            driver.find_element(By.XPATH, element).click()

    driver.find_element(By.XPATH,
                        '/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[4]/td/table[2]/tbody/tr[62]/td[2]/input[1]').click()  # выбрать

def clicks_for_cast_iron():
    driver.find_element(By.XPATH, "/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[3]/td[2]/a[1]").click()
    driver.find_element(By.XPATH,
                        "/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[4]/td/form/table/tbody/tr[1]/td[2]/select/option[4]").click()
    driver.find_element(By.XPATH,
                        "/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[4]/td/form/table/tbody/tr[3]/td[2]/input[2]").click()

    for i in range(3, 11):
        selected = [4, 5]
        if i in selected:
            element = f"/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[4]/td/form/table[2]/tbody/tr[{str(i)}]/td[6]/input"
            driver.find_element(By.XPATH, element).click()

    driver.find_element(By.XPATH,
                        "/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[4]/td/form/table[2]/tbody/tr[11]/td[2]/input").click()  ## Выбрать
    driver.find_element(By.XPATH, '/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[2]/td/table/tbody/tr/td/a').click()

def found_XPATH_START(year,month):
    driver.find_element(By.XPATH,
                        "/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[2]/td/table[1]/tbody/tr/td[1]/table/tbody/tr[4]/td/table/tbody/tr/td[1]/select/option[1]").click()
    found_month_checkbox=""
    tr=0
    tb=0
    for i in range(1, 65): ### 65+2 В СЛЕДУЮЩЕМ ГОДУ(2023)
        if i % 2 == 1:
            site_year = driver.find_element(By.XPATH,
                                            f'/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[2]/td/table[1]/tbody/tr/td[1]/table/tbody/tr[6]/td/table/tbody/tr[{str(i)}]/td[1]').text
            if site_year.lstrip() == year:
                for j in range(i, i + 2):  ### 2 строки года
                    for k in range(2, 8):  ### 6 месяцев одной строки
                        find_month = driver.find_element(By.XPATH,f"/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[2]/td/table[1]/tbody/tr/td[1]/table/tbody/tr[6]/td/table/tbody/tr[{str(j)}]/td[{str(k)}]").text
                        if  month==find_month.lstrip(): ## год и месяц нашлись
                            found_mounth_checkbox=f"/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[2]/td/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[6]/td/table/tbody/tr[{str(j)}]/td[{str(k)}]/input"
                            tr = j
                            tb = k
    return [found_month_checkbox,tr,tb]

def clicker_to_end(XPATH_CHECKBOX,tr,tb):
    for x in range(int(tb),8):
        driver.find_element(By.XPATH,f"/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[2]/td/table[1]/tbody/tr/td[1]/table/tbody/tr[6]/td/table/tbody/tr[{str(tr)}]/td[{str(x)}]/input").click()
    for i in range(tr+1,65):
        for j in range(2,8):
            driver.find_element(By.XPATH,f"/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[2]/td/table[1]/tbody/tr/td[1]/table/tbody/tr[6]/td/table/tbody/tr[{str(i)}]/td[{str(j)}]/input").click()

def to_excel(month_inp,year):
    try:
        source = driver.page_source

        source_table = bs4.BeautifulSoup(source, 'lxml')
        # print(source_table)
        ## table = soup.find("table") !!!!!!!!!!!!!!!!!!!
        ## print(soup)
        ## print(type(table))
        source_table = str(source_table)
        soup = bs4.BeautifulSoup(source_table, "lxml")
        data = pd.read_html(str(soup))
        data = data[0]
        data.to_excel(f'Чугун {month_inp.zfill(2)}.{year}.xlsx', index=False)
        table = pd.read_excel(f'Чугун {month_inp.zfill(2)}.{year}.xlsx', sheet_name='Sheet1', header=0, skiprows=17)
        table.dropna(axis=0, how="all", inplace=True)
        table.drop(table.index[[14,16,15]], axis=0, inplace=True)
        table.drop(table.columns[[0]], axis=1, inplace=True)

        table.to_excel(f'Чугун {month_inp.zfill(2)}.{year}.xlsx', index=False)

        # source_table=str(source_table)
        # soup = bs4.BeautifulSoup(source_table, "lxml")
        # data = pd.read_html(str(soup))
        # data = data[0]
        # data.to_excel('test_2.xlsx', index=False)
        # table = pd.read_excel('test_2.xlsx', sheet_name='Sheet1', header=0)
        # table.dropna(axis=0, how='all', inplace=True)
        # table.drop(table.columns[[0]], axis=1, inplace=True)
        # table.drop(table.index[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]], axis=0, inplace=True)
        # table.to_excel(f'Чугун {month_inp.zfill(2)}.{year}.xlsx', index=False)
    except:
        print("problem with unloading :(")


try:
    months = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
              9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
    year, month_inp = (input("Введите год и номер месяцa, с которого выгружаем (через пробел)\n")).split()
    start_time = time.time()
    month = months[int(month_inp)].lower()
    auth()
    clicker_to_list()
    clicks_for_metal_combine()
    clicks_for_metal_plant()
    clicks_for_cast_iron()
    XPATH_CHECKBOX = found_XPATH_START(year, month)
    clicker_to_end(XPATH_CHECKBOX[0], XPATH_CHECKBOX[1], XPATH_CHECKBOX[2])

    driver.find_element(By.XPATH,"/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[2]/td/table[1]/tbody/tr/td[1]/table/tbody/tr[8]/td/table/tbody/tr[1]/td/table/tbody/tr[6]/td[3]/input").click()
    driver.find_element(By.XPATH,"/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[2]/td/table[1]/tbody/tr/td[1]/table/tbody/tr[8]/td/table/tbody/tr[4]/td/input[1]").click()
    to_excel(month_inp,year)
    print(f"fine!!!\nTotal execution time: {time.time() - start_time} sec")
except Exception:
     print(Exception)
