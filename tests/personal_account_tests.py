'''Тесты для проверки функциональности личного кабинета.'''
from selenium.webdriver.common.by import By

import tests.locators as loc
from tools import sign_in_account

CONSTRUCTOR_HEADER = 'Соберите бургер'
SIGN_IN_FORM_TITLE = 'Вход'
PERSONAL_ACCOUNT_TEXT = (
    'В этом разделе вы можете изменить свои персональные данные'
)


def test_enter_account_with_account_link(driver, login, password):
    '''Вход в личный кабинет по ссылке «Личный кабинет».'''
    try:
        sign_in_account(driver, login, password)
        driver.find_element(by=By.XPATH, value=loc.ACCOUNT_LINK).click()
        assert (
            driver.find_element(
                by=By.XPATH, value=loc.PERSONAL_ACCOUNT
            ).text == PERSONAL_ACCOUNT_TEXT
        )
    finally:
        driver.quit()


def test_switch_from_account_with_constructor_link(driver, login, password):
    '''Переход из личного кабинета по клику на ссылку «Конструктор».'''
    try:
        sign_in_account(driver, login, password)
        driver.find_element(by=By.XPATH, value=loc.ACCOUNT_LINK).click()
        driver.find_element(by=By.XPATH, value=loc.CONSTRUCTOR_LINK).click()
        assert (
            driver.find_element(
                by=By.XPATH, value=loc.CONSTRUCT_BURGER_HEADER
            ).text == CONSTRUCTOR_HEADER
        )
    finally:
        driver.quit()


def test_switch_from_account_with_logo_link(driver, login, password):
    '''Переход из личного кабинета по клику на логотип «Stellar Burgers».'''
    try:
        sign_in_account(driver, login, password)
        driver.find_element(by=By.XPATH, value=loc.ACCOUNT_LINK).click()
        driver.find_element(by=By.XPATH, value=loc.LOGO_LINK).click()
        assert (
            driver.find_element(
                by=By.XPATH, value=loc.CONSTRUCT_BURGER_HEADER
            ).text == CONSTRUCTOR_HEADER
        )
    finally:
        driver.quit()


def test_log_out_from_account_with_exit_button(driver, login, password):
    '''Выход из личного кабинета по кнопке «Выйти».'''
    try:
        sign_in_account(driver, login, password)
        driver.find_element(by=By.XPATH, value=loc.ACCOUNT_LINK).click()
        driver.find_element(by=By.XPATH, value=loc.EXIT_BUTTON).click()
        assert (
            driver.find_element(
                by=By.XPATH, value=loc.SIGN_IN_FORM_TITLE
            ).text == SIGN_IN_FORM_TITLE
        )
    finally:
        driver.quit()
