
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from constants import ConstantsEMAIL
from locators import Locators

class TestSBurgerslogin:
    def test_login_in_accaunt(self, driver): #Позитивный тест на авторизацию через кнопку "Войти в Аккаунт" с переходом в Личный Кабинет по клику
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.AUTH_ENTER_TEXT))#найти элемент "Войти"
        driver.find_element(*Locators.EMAIL).clear()
        driver.find_element(*Locators.EMAIL).send_keys(ConstantsEMAIL.EMAIL)
        driver.find_element(*Locators.PASSWORD).clear()
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.CONSTRUCT_BURGER))#Проверка заголовка "Соберите бургер"
        driver.find_element(*Locators.CABINET_BUTTON).click()

        element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_LOGIN))
        account_email = element.get_attribute('value')#Получение значения поля с email
        assert  account_email == ConstantsEMAIL.EMAIL #Проверка Email в личном кабинете

    def test_login_via_cabinet(self,driver):#Позитивный тест на авторизацию через кнопку "Личный кабинет"
        driver.find_element(*Locators.CABINET_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.AUTH_ENTER_TEXT))#найти кнопку "Войти"
        driver.find_element(*Locators.EMAIL).clear()
        driver.find_element(*Locators.EMAIL).send_keys(ConstantsEMAIL.EMAIL)
        driver.find_element(*Locators.PASSWORD).clear()
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.CONSTRUCT_BURGER))#Проверка заголовка "Соберите бургер"
        driver.find_element(*Locators.CABINET_BUTTON).click()

        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.PROFILE_LOGIN))
        account_email = element.get_attribute('value')#Получение значения поля с email
        assert  account_email == ConstantsEMAIL.EMAIL #Проверка Email в личном кабинете

    def test_login_via_registr_form(self, driver):#Позитивный тест на авторизацию через кнопку Формы Регистрации
        driver.find_element(*Locators.CABINET_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.AUTH_ENTER_TEXT))#найти кнопку "Войти"
        driver.find_element(*Locators.REGISTRATION_BUTTON_FROM_AUTH).click()#Переход по кнопке "Зарегистрироваться"
        driver.find_element(*Locators.ENTER_BUTTON_FROM_REG_TO_AUTH).click()#Переход по кнопке "Войти" в форму авторизации
        driver.find_element(*Locators.EMAIL).clear()
        driver.find_element(*Locators.EMAIL).send_keys(ConstantsEMAIL.EMAIL)
        driver.find_element(*Locators.PASSWORD).clear()
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.CONSTRUCT_BURGER))#Проверка заголовка "Соберите бургер"
        driver.find_element(*Locators.CABINET_BUTTON).click()

        element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_LOGIN))
        account_email = element.get_attribute('value')#Получение значения поля с email
        assert  account_email == ConstantsEMAIL.EMAIL #Проверка Email в личном кабинете

    def test_login_via_restore_button(self,driver):#Позитивный тест на авторизацию через кнопку Восстановления пароля
        driver.find_element(*Locators.CABINET_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.AUTH_ENTER_TEXT))#найти кнопку "Войти"
        driver.find_element(*Locators.RESTORE_PASSWORD_BUTTON).click()#Переход по кнопке "Восстановить пароль"
        driver.find_element(*Locators.ENTER_BUTTON_FROM_REG_TO_AUTH).click()#Переход по кнопке "Войти" в форму авторизации
        driver.find_element(*Locators.EMAIL).clear()
        driver.find_element(*Locators.EMAIL).send_keys(ConstantsEMAIL.EMAIL)
        driver.find_element(*Locators.PASSWORD).clear()
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.CONSTRUCT_BURGER))#Проверка заголовка "Соберите бургер"
        driver.find_element(*Locators.CABINET_BUTTON).click()

        element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_LOGIN))
        account_email = element.get_attribute('value')#Получение значения поля с email
        assert  account_email == ConstantsEMAIL.EMAIL #Проверка Email в личном кабинете
