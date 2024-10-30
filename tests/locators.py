'''Локаторы элементов DOM для тестирования web-сервиса «Stellar Burgers».'''
from selenium.webdriver.common.by import By


class Locators:
    # УНИВЕРСАЛЬНЫЕ:
    # любая кнопка
    BUTTON = '//button[text()="{btn}"]'
    # формы «Регистрация» или «Вход»
    FORM = './/h2[text()="{form}"]/parent::div/form'
    # поля форм «Регистрация» или «Вход»
    FORM_FIELDS = FORM + '//label[text()="{field}"]/parent::div/input'
    # поля «Имя», «Логин» или «Пароль» профиля
    PROFILE_FIELDS = (
        './/li[contains(@class, "profile")]//label[text()="{field}"]'
        '/parent::div/input'
    )
    # разделы «Булки», «Соусы» или «Начинки» в конструкторе
    CATEGORIES = './/span[text()="{name}"]/parent::div'

    # ДЛЯ СОЗДАНИЯ АККАУНТА:
    # ссылка «Личный кабинет»
    ACCOUNT_LINK = By.XPATH, './/p[text()="Личный Кабинет"]'
    # ссылка «Зарегистрироваться»
    SIGN_UP_LINK = By.XPATH, './/a[text()="Зарегистрироваться"]'
    # поле ввода «Имя» формы «Регистрация»
    SIGN_UP_NAME_INPUT = (
        By.XPATH, FORM_FIELDS.format(form='Регистрация', field='Имя')
    )
    # поле ввода «Email» формы «Регистрация»
    SIGN_UP_EMAIL_INPUT = (
        By.XPATH, FORM_FIELDS.format(form='Регистрация', field='Email')
    )
    # поле ввода «Пароль» формы «Регистрация»
    SIGN_UP_PASSWORD_INPUT = (
        By.XPATH, FORM_FIELDS.format(form='Регистрация', field='Пароль')
    )
    # кнопка «Зарегистрироваться» формы «Регистрация»
    SIGN_UP_BUTTON = (
        By.XPATH, (FORM + BUTTON).format(
            form='Регистрация', btn='Зарегистрироваться'
        )
    )

    # ДЛЯ ВХОДА В АККАУНТ:
    # заголовок формы «Вход»
    SIGN_IN_FORM = By.XPATH, './/div[contains(@class, "Auth_login")]/h2'
    # поле ввода «Email» формы «Вход»
    SIGN_IN_EMAIL_INPUT = (
        By.XPATH, FORM_FIELDS.format(form='Вход', field='Email')
    )
    # поле ввода «Пароль» формы «Вход»
    SIGN_IN_PASSWORD_INPUT = (
        By.XPATH, FORM_FIELDS.format(form='Вход', field='Пароль')
    )
    # кнопка «Войти» формы «Вход»
    SIGN_IN_BUTTON = By.XPATH, (FORM + BUTTON).format(form='Вход', btn='Войти')
    # ссылка «Войти» под формой «Регистрация»
    SIGN_IN_LINK = (
        By.XPATH, './/p[text()="Уже зарегистрированы?"]/a[text()="Войти"]'
    )

    # ДЛЯ ПРОВЕРКИ ПРОФИЛЯ:
    # ссылка «Профиль»
    PROFILE_LINK = By.XPATH, './/a[text()="Профиль"]'
    # поле «Имя» профиля
    PROFILE_NAME = By.XPATH, PROFILE_FIELDS.format(field='Имя')
    # поле «Логин» профиля
    PROFILE_LOGIN = By.XPATH, PROFILE_FIELDS.format(field='Логин')
    # указатель на текст страницы личного кабинета
    PERSONAL_ACCOUNT = By.XPATH, './/p[contains(@class, "Account_text")]'
    # кнопка «Выход» в личном кабинете
    EXIT_BUTTON = By.XPATH, BUTTON.format(btn='Выход')

    # ЭЛЕМЕНТЫ НА ГЛАВНОЙ СТРАНИЦЕ:
    # кнопка «Войти в аккаунт»
    ENTER_ACCOUNT_BUTTON = By.XPATH, BUTTON.format(btn='Войти в аккаунт')
    # ссылка «Конструктор»
    CONSTRUCTOR_LINK = By.XPATH, './/p[text()="Конструктор"]'
    # ссылка-логотип «Stellar Burgers»
    LOGO_LINK = By.XPATH, './/div[contains(@class, "log")]/a[@href="/"]'
    # заголовок «Соберите бургер»
    CONSTRUCT_BURGER = (
        By.XPATH, './/section[contains(@class, "ingredients")]/h1'
    )
    # раздел «Булки» в конструкторе
    BUNS = By.XPATH, CATEGORIES.format(name='Булки')
    # раздел «Соусы» в конструкторе
    SAUCES = By.XPATH, CATEGORIES.format(name='Соусы')
    # раздел «Начинки» в конструкторе
    TOPPINGS = By.XPATH, CATEGORIES.format(name='Начинки')

    # ОСТАЛЬНОЕ:
    # предупреждающее сообщение «Некорректный пароль»
    INVALID_PASSWORD_WARNING = (
        By.XPATH,
        FORM.format(form='Регистрация') + '//p[contains(@class, "error")]'
    )
    # ссылка «Восстановить пароль» под формой «Вход»
    RESTORE_PASSWORD_LINK = (
        By.XPATH,
        './/p[text()="Забыли пароль?"]/a[text()="Восстановить пароль"]'
    )
    # ссылка «Войти» под формой «Восстановление пароля»
    REMEMBER_PASSWORD_SIGN_IN_LINK = (
        By.XPATH, './/p[text()="Вспомнили пароль?"]/a[text()="Войти"]'
    )
    # кнопка «Оформить заказ» в секции "корзина"
    BASKET_BUTTON = By.XPATH, BUTTON.format(btn="Оформить заказ")


if __name__ == '__main__':
    print(Locators.BLOCKER)
