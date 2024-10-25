'''Локаторы элементов DOM для тестов.'''
# кнопка «Войти в аккаунт»
ENTER_ACCOUNT_BTN = './/button[text()="Войти в аккаунт"]'
# ссылка «Личный кабинет»
ACCOUNT_LINK = './/a[@href="/account"]'
# текст ссылки «Зарегистрироваться»
SIGN_UP_LINK_TEXT = 'Зарегистрироваться'
# поле ввода «Имя» формы регистрации
SIGN_UP_NAME_INPUT = '''\
.//div/h2[text()="Регистрация"]/parent::div//label[text()="Имя"]/\
parent::div/input
'''
# поле ввода «Email» формы регистрации
SIGN_UP_EMAIL_INPUT = '''\
.//div/h2[text()="Регистрация"]/parent::div//label[text()="Email"]/\
parent::div/input
'''
# поле ввода «Пароль» формы регистрации
SIGN_UP_PASSWORD_INPUT = '''\
.//div/h2[text()="Регистрация"]/parent::div//input[@type="password"]
'''
# кнопка «Зарегистрироваться»
SIGN_UP_BTN = './/button[text()="Зарегистрироваться"]'
# кнопка «Войти»
LOG_IN_BTN = './/button[text()="Войти"]'
# поле ввода «Email» формы входа в аккаунт
SIGN_IN_EMAIL_INPUT = '''\
.//div/h2[text()="Вход"]/parent::div//label[text()="Email"]/parent::div/input
'''
# поле ввода «Пароль» формы входа в аккаунт
SIGN_IN_PASSWORD_INPUT = '''\
.//div/h2[text()="Вход"]/parent::div//input[@type="password"]
'''
# предупреждающее сообщение «Некорректный пароль»
INVALID_PASSWORD_WARNING = './/p[@class="input__error text_type_main-default"]'
# текст ссылки «Профиль»
PROFILE_LINK_TEXT = 'Профиль'
# поле профиля «Имя»
PROFILE_NAME = './/li//label[text()="Имя"]/parent::div/input'
# поле профиля «Логин»
PROFILE_LOGIN = './/li//label[text()="Логин"]/parent::div/input'
