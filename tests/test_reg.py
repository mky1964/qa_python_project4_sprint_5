from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

faker = Faker()
from constants import Constants
from constants import ConstantsURL
from locators import Locators


class TestSBurgersRegPositive:
    def test_reg_positive(self, driver): #Позитивный тест на регистрацию
        email = faker.email()
        password = Constants.PASSWORD
        name = 'Петя'
        driver.find_element(*Locators.CABINET_BUTTON).click()#Клик "Личный Кабинет"
        driver.find_element(*Locators.CABINET_REGISTRATION_BUTTON).click()#Клик "Зарегистрироваться"
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REGISTRATION_NAME_PLACEHOLDER_NAME))
        driver.find_element(*Locators.REGISTRATION_NAME_PLACEHOLDER).clear()
        driver.find_element(*Locators.REGISTRATION_NAME_PLACEHOLDER).send_keys(name)#Ввод Имя
        driver.find_element(*Locators.REGISTRATION_EMAIL_PLACEHOLDER).clear()
        driver.find_element(*Locators.REGISTRATION_EMAIL_PLACEHOLDER).send_keys(email)
        driver.find_element(*Locators.REGISTRATION_PASSWORD_PLACEHOLDER).clear()#Ввод Пароль
        driver.find_element(*Locators.REGISTRATION_PASSWORD_PLACEHOLDER).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_REG_BUTTON).click()#Клик на Зарегистрироваться

        #form_name = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//h2[text() = "Вход"]'))).text
        assert  WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.AUTH_ENTER_TEXT))#Проверка наличия  элемента с текстом 'Вход' заголовка в форме авторизации

class TestSBurgersRegNegativePass:
    def test_reg_negative_password(self,driver):# Негативный тест на ввод пароля (вводиться 4 символа
        email = faker.email()
        name ='Вася'

        password = '1234'# 4 символа в password
        driver.find_element(*Locators.CABINET_BUTTON).click()  # Кликаем "Личный Кабинет"
        driver.find_element(*Locators.CABINET_REGISTRATION_BUTTON).click()  # Кликаем "Зарегистрироваться"
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located(Locators.REGISTRATION_NAME_PLACEHOLDER_NAME))
        driver.find_element(*Locators.REGISTRATION_NAME_PLACEHOLDER).clear()
        driver.find_element(*Locators.REGISTRATION_NAME_PLACEHOLDER).send_keys(name)  # Ввод Имя
        driver.find_element(*Locators.REGISTRATION_EMAIL_PLACEHOLDER).clear()
        driver.find_element(*Locators.REGISTRATION_EMAIL_PLACEHOLDER).send_keys(email)
        driver.find_element(*Locators.REGISTRATION_PASSWORD_PLACEHOLDER).clear()
        driver.find_element(*Locators.REGISTRATION_PASSWORD_PLACEHOLDER).send_keys(password) #ввод Пароль
        driver.find_element(*Locators.REGISTRATION_REG_BUTTON).click()  # Клик на Зарегистрироваться

        alert_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.INCORRECT_REG_TEXT)).text

        assert alert_text == 'Некорректный пароль'  # Проверка сообщения




