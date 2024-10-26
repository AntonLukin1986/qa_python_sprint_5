'''Тесты для проверки функциональности регистрации нового пользователя.'''
from selenium.webdriver.common.by import By

from . import locators as loc


INVALID_PASSWORD = '1'
USER_NAME = 'Пользователь'      ##########################################################################
WARNING = 'Некорректный пароль'


def create_account(driver, login, password):
    '''Создание нового пользователя.'''
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
            getattr(driver.find_element(by=By.XPATH, value=value), method)()
        else:
            getattr(driver.find_element(by=By.XPATH, value=value), method)(text)


def log_in_account(driver, login, password):
    '''Вход в аккаунт пользователя.'''
    find_element_args = (
        (loc.SIGN_IN_EMAIL_INPUT, 'send_keys', login),
        (loc.SIGN_IN_PASSWORD_INPUT, 'send_keys', password),
        (loc.SIGN_IN_BUTTON, 'click', None)
    )
    for value, method, text in find_element_args:
        if text is None:
            getattr(driver.find_element(by=By.XPATH, value=value), method)()
        else:
            getattr(driver.find_element(by=By.XPATH, value=value), method)(text)


def test_sign_up_new_account_created(driver, login, password):
    '''Успешная регистрация нового пользователя.'''
    create_account(driver, login, password)
    log_in_account(driver, login, password)
    driver.find_element(by=By.XPATH, value=loc.ACCOUNT_LINK).click()
    driver.find_element(by=By.XPATH, value=loc.PROFILE_LINK).click()
    checks = (loc.PROFILE_NAME, USER_NAME), (loc.PROFILE_LOGIN, login)
    for value, expected in checks:
        assert (
            driver.find_element(by=By.XPATH, value=value).
            get_attribute(name='value') == expected
        )
    driver.quit()


def test_sign_up_with_invalid_password_warning(driver):
    '''Предупреждающее сообщение о недопустимом пароле при регистрации
    пользователя.'''
    driver.find_element(by=By.XPATH, value=loc.ACCOUNT_LINK).click()
    driver.find_element(by=By.XPATH, value=loc.SIGN_UP_LINK).click()
    driver.find_element(
        by=By.XPATH, value=loc.SIGN_UP_PASSWORD_INPUT
    ).send_keys(INVALID_PASSWORD)
    driver.find_element(by=By.XPATH, value=loc.SIGN_UP_BUTTON).click()
    assert (
        driver.find_element(by=By.XPATH, value=loc.INVALID_PASSWORD_WARNING).
        text == WARNING
    )
    driver.quit()
