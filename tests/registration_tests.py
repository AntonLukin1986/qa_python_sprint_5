'''Тесты для проверки функциональности регистрации нового пользователя.'''
from selenium.webdriver.common.by import By

import tests.locators as loc
from tools import sign_in_account, USER_NAME

INVALID_PASSWORD = '1'
WARNING = 'Некорректный пароль'


def test_sign_up_new_account_created(driver, login, password):
    '''Успешная регистрация нового пользователя.'''
    try:
        sign_in_account(driver, login, password)
        driver.find_element(by=By.XPATH, value=loc.ACCOUNT_LINK).click()
        driver.find_element(by=By.XPATH, value=loc.PROFILE_LINK).click()
        checks = (loc.PROFILE_NAME, USER_NAME), (loc.PROFILE_LOGIN, login)
        for value, expected in checks:
            assert (
                driver.find_element(by=By.XPATH, value=value).
                get_attribute(name='value') == expected
            )
    finally:
        driver.quit()


def test_sign_up_with_invalid_password_warning(driver, *args):
    '''Предупреждающее сообщение о недопустимом пароле при регистрации
    пользователя.'''
    try:
        driver.find_element(by=By.XPATH, value=loc.ACCOUNT_LINK).click()
        driver.find_element(by=By.XPATH, value=loc.SIGN_UP_LINK).click()
        driver.find_element(
            by=By.XPATH, value=loc.SIGN_UP_PASSWORD_INPUT
        ).send_keys(INVALID_PASSWORD)
        driver.find_element(by=By.XPATH, value=loc.SIGN_UP_BUTTON).click()
        assert (
            driver.find_element(
                by=By.XPATH, value=loc.INVALID_PASSWORD_WARNING
            ).text == WARNING
        )
    finally:
        driver.quit()
