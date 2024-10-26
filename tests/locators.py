'''Локаторы элементов DOM для тестов.'''
# УНИВЕРСАЛЬНЫЕ:
# любая кнопка
BUTTON = '//button[text()="{btn}"]'
# формы «Регистрация» или «Вход»
FORM = './/h2[text()="{form}"]/parent::div/form'
# поля форм «Регистрация» или «Вход»
FORM_FIELDS = FORM + '//label[text()="{field}"]/parent::div/input'
# поля «Имя», «Логин» или «Пароль» профиля
PROFILE_FIELDS = '''\
.//li[contains(@class, "profile")]//label[text()="{field}"]/parent::div/input
'''
# разделы «Булки», «Соусы» или «Начинки» в конструкторе
CATEGORIES = '''\
.//span[text()="{name}"]/parent::div
'''

# ДЛЯ СОЗДАНИЯ АККАУНТА:
# ссылка «Личный кабинет»
ACCOUNT_LINK = './/a[@href="/account"]/p[text()="Личный Кабинет"]'
# ссылка «Зарегистрироваться»
SIGN_UP_LINK = './/a[@href="/register" and text()="Зарегистрироваться"]'
# поле ввода «Имя» формы «Регистрация»
SIGN_UP_NAME_INPUT = FORM_FIELDS.format(form='Регистрация', field='Имя')
# поле ввода «Email» формы «Регистрация»
SIGN_UP_EMAIL_INPUT = FORM_FIELDS.format(form='Регистрация', field='Email')
# поле ввода «Пароль» формы «Регистрация»
SIGN_UP_PASSWORD_INPUT = FORM_FIELDS.format(form='Регистрация', field='Пароль')
# кнопка «Зарегистрироваться» формы «Регистрация»
SIGN_UP_BUTTON = (FORM + BUTTON).format(
    form='Регистрация', btn='Зарегистрироваться'
)

# ДЛЯ ВХОДА В АККАУНТ:
# заголовок формы «Вход»
SIGN_IN_FORM_TITLE = './/h2[text()="Вход"]'
# поле ввода «Email» формы «Вход»
SIGN_IN_EMAIL_INPUT = FORM_FIELDS.format(form='Вход', field='Email')
# поле ввода «Пароль» формы «Вход»
SIGN_IN_PASSWORD_INPUT = FORM_FIELDS.format(form='Вход', field='Пароль')
# кнопка «Войти» формы «Вход»
SIGN_IN_BUTTON = (FORM + BUTTON).format(form='Вход', btn='Войти')

# ДЛЯ ПРОВЕРКИ ПРОФИЛЯ
# ссылка «Профиль»
PROFILE_LINK = './/a[@href="/account/profile" and text()="Профиль"]'
# поле «Имя» профиля
PROFILE_NAME = PROFILE_FIELDS.format(field='Имя')
# поле «Логин» профиля
PROFILE_LOGIN = PROFILE_FIELDS.format(field='Логин')

# предупреждающее сообщение «Некорректный пароль»
INVALID_PASSWORD_WARNING = (
    FORM.format(form='Регистрация') +
    '//p[@class="input__error text_type_main-default"]'
)
# кнопка «Войти в аккаунт» на главной странице
ENTER_ACCOUNT_BUTTON = BUTTON.format(btn='Войти в аккаунт')
# ссылка «Войти» под формой «Регистрация»
SIGN_IN_LINK = '''\
.//p[text()="Уже зарегистрированы?"]/a[@href="/login" and text()="Войти"]
'''
# ссылка «Восстановить пароль» под формой «Вход»
RESTORE_PASSWORD_LINK = '''\
.//p[text()="Забыли пароль?"]/a[@href="/forgot-password" and \
text()="Восстановить пароль"]
'''
# ссылка «Войти» под формой «Восстановление пароля»
REMEMBER_PASSWORD_SIGN_IN_LINK = '''\
.//p[text()="Вспомнили пароль?"]/a[@href="/login" and text()="Войти"]
'''
# ссылка «Конструктор» на главной странице
CONSTRUCTOR_LINK = './/a[@href="/"]/p[text()="Конструктор"]'
# ссылка-логотип «Stellar Burgers» на главной странице
LOGO_LINK = './/div[contains(@class, "log")]/a[@href="/"]'
# заголовок «Соберите бургер»
CONSTRUCT_BURGER_HEADER = './/h1[text()="Соберите бургер"]'
# кнопка «Выход» в личном кабинете
EXIT_BUTTON = BUTTON.format(btn='Выход')
# раздел «Булки» в конструкторе
BUNS = CATEGORIES.format(name='Булки')
# раздел «Соусы» в конструкторе
SAUCES = CATEGORIES.format(name='Соусы')
# раздел «Начинки» в конструкторе
TOPPINGS = CATEGORIES.format(name='Начинки')
# раздел «Булки» в конструкторе для проверки активности


if __name__ == '__main__':
    print(BUNS)
