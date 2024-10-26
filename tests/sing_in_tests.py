'''Тесты для проверки функциональности входа в аккаунт.'''
from selenium.webdriver.common.by import By

from . import locators as loc
from .registration_tests import create_account, log_in_account

HOME_URL = 'https://stellarburgers.nomoreparties.site/'      ######################################################################
USER_NAME = 'Пользователь'                               ##########################################################################


def test_sign_in_with_enter_account_button(driver, login, password):
    '''Вход в аккаунт по кнопке «Войти в аккаунт» на главной странице.'''
    create_account(driver, login, password)
    driver.get(url=HOME_URL)
    driver.find_element(by=By.XPATH, value=loc.ENTER_ACCOUNT_BUTTON).click()
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


def test_sign_in_with_account_link(driver, login, password):
    '''Вход в аккаунт по ссылке «Личный кабинет».'''
    create_account(driver, login, password)
    driver.get(url=HOME_URL)
    driver.find_element(by=By.XPATH, value=loc.ACCOUNT_LINK).click()
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


def test_sign_in_with_link_in_registration_form(driver, login, password):
    '''Вход в аккаунт по ссылке «Войти» формы регистрации.'''
    create_account(driver, login, password)
    driver.get(url=HOME_URL)
    driver.find_element(by=By.XPATH, value=loc.ENTER_ACCOUNT_BUTTON).click()
    driver.find_element(by=By.XPATH, value=loc.SIGN_UP_LINK).click()
    driver.find_element(by=By.XPATH, value=loc.SIGN_IN_LINK).click()
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


def test_sign_in_with_link_in_restore_password_form(driver, login, password):
    '''Вход в аккаунт по ссылке «Войти» формы восстановления пароля.'''
    create_account(driver, login, password)
    driver.get(url=HOME_URL)
    driver.find_element(by=By.XPATH, value=loc.ENTER_ACCOUNT_BUTTON).click()
    driver.find_element(by=By.XPATH, value=loc.RESTORE_PASSWORD_LINK).click()
    driver.find_element(by=By.XPATH, value=loc.REMEMBER_PASSWORD_SIGN_IN_LINK).click()
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
