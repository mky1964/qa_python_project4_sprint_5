
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants
from locators import Locators

class TestSBurgersCabinet:
    def test_pass_cabinet_to_constructor(self,login_and_pass_to_cabinet):#Позитивный тест на  переход из Личного Кабинета в Конструктор
        driver = login_and_pass_to_cabinet# Авторизация и переход по клику в ЛичныйКабинет

        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.PROFILE_LOGIN))#ожидание "LOGIN" в Профиле
        driver.find_element(*Locators.CABINET_CONSTRUCTOR_BUTTON).click()#Переход в Конструктор

        print(WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.CONSTRUCT_BURGER)))
        assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.CONSTRUCT_BURGER))#Поверка наличия элемента "Соберите бургер"


    def test_pass_cabinet_exit_button(self,login_and_pass_to_cabinet):#Позитивный тест на  выход из личного кабинета
        driver = login_and_pass_to_cabinet# Авторизация и переход по клику в Личный Кабинет

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_LOGIN))#ожидание "LOGIN" в Профиле
        driver.find_element(*Locators.CABINET_EXIT_BUTTON).click()#Переход кликом по ВЫХОД

        assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.AUTH_ENTER_TEXT))#Проверка наличия элемента ВХОД в форме авторизации


    def test_pass_cabinet_exit_logo(self,login_and_pass_to_cabinet):#Позитивный тест на  переход из Личного Кабинета по клику ЛОГО
        driver = login_and_pass_to_cabinet# Авторизация и переход по клику в ЛичныйКабинет

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_LOGIN))#ожидание "LOGIN" в Профиле
        driver.find_element(*Locators.CABINET_LOGO_BUTTON).click()#Переход по клику ЛОГО

        assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.CONSTRUCT_BURGER))#Поверка наличия элемента "Соберите бургер"