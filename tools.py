'''Вспомогательные инструменты для тестов.'''
import random
import string

from selenium import webdriver
from selenium.webdriver.common.by import By

from tests import locators as loc

HOME_URL = 'https://stellarburgers.nomoreparties.site/'
USER_NAME = 'Пользователь'


def generate_password():
    '''Генератор паролей.'''
    length = random.randint(6, 10)
    chars = string.digits + string.ascii_letters + string.punctuation
    return ''.join(random.choices(chars, k=length))


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


def chrome_driver_init(hide, url=HOME_URL):
    '''Создаёт драйвер браузера Google Chrome, открывает заданную страницу.'''
    options = webdriver.ChromeOptions()
    options.add_argument(argument='--headless' if hide else 'start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(time_to_wait=3)
    driver.get(url)
    return driver


def create_account(*, driver, hide, login, password):
    '''Создание нового аккаунта.'''
    print('Создание нового аккаунта...')
    driver = driver(hide)
    try:
        find_element_args = (
            (loc.ACCOUNT_LINK, 'click', None),
            (loc.SIGN_UP_LINK, 'click', None),
            (loc.SIGN_UP_NAME_INPUT, 'send_keys', USER_NAME),
            (loc.SIGN_UP_EMAIL_INPUT, 'send_keys', login),
            (loc.SIGN_UP_PASSWORD_INPUT, 'send_keys', password),
            (loc.SIGN_UP_BUTTON, 'click', None)
        )
        for value, method, text in find_element_args:
            if text is None:
                getattr(
                    driver.find_element(by=By.XPATH, value=value), method
                )()
            else:
                getattr(
                    driver.find_element(by=By.XPATH, value=value), method
                )(text)
    finally:
        driver.quit()


def sign_in_account(driver, login, password):
    '''Вход в аккаунт пользователя.'''
    find_element_args = (
        (loc.ACCOUNT_LINK, 'click', None),
        (loc.SIGN_IN_EMAIL_INPUT, 'send_keys', login),
        (loc.SIGN_IN_PASSWORD_INPUT, 'send_keys', password),
        (loc.SIGN_IN_BUTTON, 'click', None)
    )
    for value, method, text in find_element_args:
        if text is None:
            getattr(driver.find_element(by=By.XPATH, value=value), method)()
        else:
            getattr(
                driver.find_element(by=By.XPATH, value=value), method
            )(text)


if __name__ == '__main__':
    print('Логин: ', generate_login())
    print('Пароль:', generate_password())
