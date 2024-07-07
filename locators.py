from selenium.webdriver.common.by import By


class Locators:
    EMAIL = (By.XPATH, "//input[@name='name']")#Поле   Email  формы авторизации
    PASSWORD = (By.XPATH, "//input[@type='password']") #Поле   PASSWORD  формы авторизации
    AUTH_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")# кнопка ввода при авторизации
    ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")#Кнопка аккаунта из главной страницы
    CABINET_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")#Кнопка личного кабинета из главной страницы
    PROFILE_LOGIN = (By.XPATH, '//li[2][@class="Profile_profileListItem__2th0t mb-6"]//input')#LOGIN в Профиле
    CABINET_CONSTRUCTOR_BUTTON = (By.XPATH,  '//a[@class="AppHeader_header__link__3D_hX" and @href="/"]' )#Кнопка перехода из ЛК в Корструктор
    CABINET_LOGO_BUTTON = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]/a[@href="/"]')#Кнопка LOGO в конструкторе ("//a[@class='AppHeader_header__link__3D_hX' and @href='/']")
    CABINET_EXIT_BUTTON = (By.XPATH, "//button[@class ='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")#Кнопка ВЫХОД из ЛК
    AUTH_ENTER_TEXT = (By.XPATH, '//main//h2[text()="Вход"]')#Текст ВХОД в форме авторизации
    CONSTRUCT_BURGER = (By.XPATH, '//h1[text()="Соберите бургер"]')#Элемент "Соберите бургер" в Конструкторе
    CABINET_REGISTRATION_BUTTON = (By.XPATH, '//a[@href="/register"]')#Кнопка ЗАРЕГИСТРИРОВАТЬСЯ в ЛК
    REGISTRATION_NAME_PLACEHOLDER_NAME =(By.XPATH, '//label[text()="Имя"]')#Название плейсхолдера "Имя" в форме регистрации
    REGISTRATION_NAME_PLACEHOLDER = (By.XPATH, '//fieldset[1]//input')#плейсхолдеh "Имя" в форме регистрации
    REGISTRATION_EMAIL_PLACEHOLDER = (By.XPATH, '//fieldset[2]//input')#плейсхолдеh "Email" в форме регистрации
    REGISTRATION_PASSWORD_PLACEHOLDER =(By.XPATH,'//fieldset[3]//input' )#плейсхолдеh "Пароль" в форме регистрации
    REGISTRATION_REG_BUTTON = (By.XPATH, '//button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')#Кнопка Зарегистрироваться в форме Регистрация
    INCORRECT_REG_TEXT = (By.XPATH, "//p[@class='input__error text_type_main-default']")#Предупреждение  "Не корректный Пароль"
    REGISTRATION_BUTTON_FROM_AUTH = (By.XPATH, '//a[@href="/register"]')#Регистрация через кнопку регистрации фв форме Авторизации
    ENTER_BUTTON_FROM_REG_TO_AUTH = (By.XPATH, '//a[@href="/login"]')#Кнопка ВХОД из Регистрации в Авторизацию
    RESTORE_PASSWORD_BUTTON = (By.XPATH, '//a[@href="/forgot-password"]')#Кнопка Восстановить Пароль
    FILLINGS_BUTTON = (By.XPATH, '//span[text()="Начинки"]')#Кнопка Начинки
    SAUCES_BUTTON = (By.XPATH, '//span[text()="Соусы"]')#Кнопка Соусы
    BREAD_BUTTON = (By.XPATH, '//span[text()="Булки"]')#Кнопка Булки
    BREAD_BUTTON_STATUS =(By.XPATH, '//span[text()="Булки"]/parent::div')#Статус кнопки Булки
    SAUCES_BUTTON_STATUS =(By.XPATH, '//span[text()="Соусы"]/parent::div')#Статус кнопки Соусы
    FILLINGS_BUTTON_STATUS =(By.XPATH, '//span[text()="Начинки"]/parent::div')#Статус кнопки Начинки