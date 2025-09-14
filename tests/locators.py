from selenium.webdriver.common.by import By

# Главная страница
MAIN_PAGE_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")

# Форма регистрации
REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
REGISTER_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
REGISTER_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
REGISTER_PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
REGISTER_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")

# Форма входа
LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")
LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")
LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

# Форма восстановления пароля
FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
FORGOT_PASSWORD_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")

# Личный кабинет
PROFILE_LINK = (By.XPATH, "//a[contains(@class, 'Account_link') and text()='Профиль']")
LOGOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button') and text()='Выход']")

# Конструктор
BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")
SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")
FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")
ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]")

# Прочие элементы
ERROR_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")
ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
SUCCESS_MESSAGE = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")