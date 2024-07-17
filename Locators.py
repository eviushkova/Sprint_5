from selenium.webdriver.common.by import By


class Locators:
    INPUT_NAME = By.XPATH, "//label[text()='Имя']/following-sibling::input"  # Поле ввода имени
    EMAIL_INPUT = By.XPATH, ".//label[text()='Email']/following-sibling::input"  # Поле ввода email
    PASSWORD_INPUT = By.XPATH, ".//label[text()='Пароль']/following-sibling::input"  # Поле ввода пароля
    REGISTER_BUTTON = By.XPATH, ".//button[text()='Зарегистрироваться']"  # Кнопка "Зарегистрироваться"
    LOGIN_BUTTON = By.XPATH, (".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                              "button_button_size_medium__3zxIa']")  # Кнопка "Войти"
    LOGIN_INPUT = By.XPATH, ".//label[text()='Логин']/following-sibling::input"  # Поле ввода "Логин" в личном кабинете
    ACCOUNT_LINK = By.XPATH, ".//a[@href='/account']" # Ссылка на личный кабинет
    INPUT_ERROR = By.XPATH, ".//p[@class='input__error text_type_main-default']"  # Ошибка при вводе невалидного пароля
    LOGIN_BUTTON_MAIN_PAGE = By.XPATH, (".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                                        "button_button_size_large__G21Vg']")  # Кнопка "Войти" на главной странице
    LOGIN_BUTTON_REGISTRATION_AND_FORGOT_PASSWORD_PAGE = By.XPATH, ".//a[@href='/login']"  # Кнопка "Войти" на
    # странице регистрации и странице восстановления пароля
    CONSTRUCTOR_BUTTON = By.XPATH, ".//p[text()='Конструктор']" # Кнопка перехода в раздел конструктора
    LOGOUT_BUTTON = By.XPATH, ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"  # Кнопка "Выход"
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, ".//p[text()='Личный Кабинет']"  # Кнопка "Личный кабинет"
    LOGO_BUTTON = By.XPATH, ".//a[@href='/']"  # Кнопка логотипа
    BUNS_TAB = By.XPATH, ".//span[text()='Булки']/parent::div"  # Вкладка "Булки"
    SAUCES_TAB = By.XPATH, ".//span[text()='Соусы']/parent::div"  # Вкладка "Соусы"
    FILLINGS_TAB = By.XPATH, ".//span[text()='Начинки']/parent::div"  # Вкладка "Начинки"


