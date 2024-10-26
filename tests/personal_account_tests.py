'''Тесты для проверки функциональности личного кабинета.'''
from selenium.webdriver.common.by import By

from . import locators as loc
from .registration_tests import create_account, log_in_account

HOME_URL = 'https://stellarburgers.nomoreparties.site/'      ######################################################################
USER_NAME = 'Пользователь'                               ##########################################################################
CONSTRUCTOR_HEADER = 'Соберите бургер'
SIGN_IN_FORM_TITLE = 'Вход'


def test_enter_account_with_account_link(driver, login, password):
    '''Вход в личный кабинет по ссылке «Личный кабинет».'''
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


def test_switch_from_account_with_constructor_link(driver, login, password):
    '''Переход из личного кабинета по клику на ссылку «Конструктор».'''
    create_account(driver, login, password)
    log_in_account(driver, login, password)
    driver.find_element(by=By.XPATH, value=loc.ACCOUNT_LINK).click()
    driver.find_element(by=By.XPATH, value=loc.CONSTRUCTOR_LINK).click()
    assert (
        driver.find_element(
            by=By.XPATH, value=loc.CONSTRUCT_BURGER_HEADER
        ).text == CONSTRUCTOR_HEADER
    )
    driver.quit()


def test_switch_from_account_with_logo_link(driver, login, password):
    '''Переход из личного кабинета по клику на логотип «Stellar Burgers».'''
    create_account(driver, login, password)
    log_in_account(driver, login, password)
    driver.find_element(by=By.XPATH, value=loc.ACCOUNT_LINK).click()
    driver.find_element(by=By.XPATH, value=loc.LOGO_LINK).click()
    assert (
        driver.find_element(
            by=By.XPATH, value=loc.CONSTRUCT_BURGER_HEADER
        ).text == CONSTRUCTOR_HEADER
    )
    driver.quit()


def test_log_out_from_account_with_exit_button(driver, login, password):
    '''Выход из личного кабинета по кнопке «Выйти».'''
    create_account(driver, login, password)
    log_in_account(driver, login, password)
    driver.find_element(by=By.XPATH, value=loc.ACCOUNT_LINK).click()
    driver.find_element(by=By.XPATH, value=loc.EXIT_BUTTON).click()
    assert (
        driver.find_element(
            by=By.XPATH, value=loc.SIGN_IN_FORM_TITLE
        ).text == SIGN_IN_FORM_TITLE
    )
    driver.quit()
