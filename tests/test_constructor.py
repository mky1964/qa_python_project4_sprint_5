

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import ConstantsURL
from locators import Locators

class TestSBurgersConstructor:
    def test_pass_to_sauce_constructor(self, login_and_pass_to_cabinet):#Переход в Конструкторе в раздел Соусы
        driver = login_and_pass_to_cabinet# Авторизация и переход по клику в ЛичныйКабинет

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_LOGIN))
        driver.find_element(*Locators.CABINET_CONSTRUCTOR_BUTTON).click()#Переход в Конструктор
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.SAUCES_BUTTON)).click()#Клик "Соусы"

        assert WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_attribute(Locators.SAUCES_BUTTON_STATUS,  "class", "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"))


    def test_pass_to_fillings_constructor(self, login_and_pass_to_cabinet):#Переход в Конструкторе в раздел Начинки
        driver = login_and_pass_to_cabinet# Авторизация и переход по клику в ЛичныйКабинет

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_LOGIN))
        driver.find_element(*Locators.CABINET_CONSTRUCTOR_BUTTON).click()#Переход в Конструктор
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.FILLINGS_BUTTON)).click()#Клик "Начинки"

        assert WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_attribute(Locators.FILLINGS_BUTTON_STATUS,  "class", "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"))

    def test_pass_to_bread_constructor(self, login_and_pass_to_cabinet):#Переход в Конструкторе в раздел Булки
        driver = login_and_pass_to_cabinet# Авторизация и переход по клику в ЛичныйКабинет

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_LOGIN))
        driver.find_element(*Locators.CABINET_CONSTRUCTOR_BUTTON).click()#Переход в Конструктор
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.FILLINGS_BUTTON)).click()#Клик "Начинки"
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.BREAD_BUTTON)).click()#Клик "Булки"

        assert WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_attribute(Locators.BREAD_BUTTON_STATUS,  "class", "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"))