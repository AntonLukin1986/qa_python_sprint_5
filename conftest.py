'''Вспомогательные инструменты для тестов web-сервиса «Stellar Burgers».'''
import random
import string

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import Locators as loc


@pytest.fixture(scope='session')
def user_name():
    '''Имя пользователя существующего аккаунта.'''
    return 'Антон'


@pytest.fixture(scope='session')
def email():
    '''Логин существующего аккаунта.'''
    return 'antonsprint5@mail.ru'


@pytest.fixture(scope='session')
def password():
    '''Пароль существующего аккаунта.'''
    return "You'llNeverGuess"


@pytest.fixture(scope='class')
def active():
    '''Маркер активной категории конструктора.'''
    return 'current'


@pytest.fixture(scope='class')
def constructor_header():
    '''Заголовок блока конструктора.'''
    return 'Соберите бургер'


@pytest.fixture(scope='class')
def personal_account_text():
    '''Текст в личном кабинете.'''
    return 'В этом разделе вы можете изменить свои персональные данные'


@pytest.fixture(scope='class')
def sign_in_form_title():
    '''Заголовок формы авторизации.'''
    return 'Вход'


@pytest.fixture(scope='class')
def invalid_password():
    '''Недопустимый пароль.'''
    return '1'


@pytest.fixture(scope='class')
def warning():
    '''Предупреждение о недопустимом пароле.'''
    return 'Некорректный пароль'


@pytest.fixture(scope='function')
def generate_password():
    '''Генератор паролей.'''
    length = random.randint(6, 10)
    chars = string.digits + string.ascii_letters + string.punctuation
    return ''.join(random.choices(chars, k=length))


@pytest.fixture(scope='function')
def generate_login():
    '''Генератор логинов.'''
    prefix = {
        'chars': string.digits + string.ascii_lowercase,
        'min_max_len': (3, 10),
        'sep': '@'
    }
    domain = {
        'chars': string.ascii_lowercase,
        'min_max_len': (2, 7),
        'sep': '.'
    }
    zone = {
        'chars': string.ascii_lowercase,
        'min_max_len': (2, 3),
        'sep': ''
    }
    login = ''
    for segment in prefix, domain, zone:
        chars = segment['chars']
        length = random.randint(*segment['min_max_len'])
        login += ''.join(random.choices(chars, k=length)) + segment['sep']
    return login


@pytest.fixture(scope='function')
def driver():
    '''Создаёт драйвер браузера Google Chrome, открывает домашнюю страницу
    web-сервиса «Stellar Burgers».'''
    options = webdriver.ChromeOptions()
    options.add_argument(argument='--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.get('https://stellarburgers.nomoreparties.site/')
    return driver


@pytest.fixture(scope='function')
def log_in(driver, email, password):
    '''Авторизация пользователя.'''
    driver.find_element(*loc.ACCOUNT_LINK).click()
    driver.find_element(*loc.SIGN_IN_EMAIL_INPUT).send_keys(email)
    driver.find_element(*loc.SIGN_IN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*loc.SIGN_IN_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(loc.BASKET_BUTTON)
    )
