'''Тесты для проверки функциональности входа в аккаунт.'''
from selenium.webdriver.common.by import By

import tests.locators as loc
from tools import sign_in_account

BUTTON_TEXT_BEFORE = 'Войти в аккаунт'
BUTTON_TEXT_AFTER = 'Оформить заказ'


def test_sign_in_with_enter_account_button(driver, login, password):
    '''Вход в аккаунт по кнопке «Войти в аккаунт» на главной странице.'''
    try:
        button_before = driver.find_element(
            by=By.XPATH, value=loc.ENTER_ACCOUNT_BUTTON
        ).text
        driver.find_element(
            by=By.XPATH, value=loc.ENTER_ACCOUNT_BUTTON
        ).click()
        sign_in_account(driver, login, password)
        button_after = driver.find_element(
            by=By.XPATH, value=loc.BASKET_BUTTON
        ).text
        assert (button_before == BUTTON_TEXT_BEFORE and
                button_after == BUTTON_TEXT_AFTER)
    finally:
        driver.quit()


def test_sign_in_with_account_link(driver, login, password):
    '''Вход в аккаунт по ссылке «Личный кабинет».'''
    try:
        button_before = driver.find_element(
            by=By.XPATH, value=loc.ENTER_ACCOUNT_BUTTON
        ).text
        driver.find_element(by=By.XPATH, value=loc.ACCOUNT_LINK).click()
        sign_in_account(driver, login, password)
        button_after = driver.find_element(
            by=By.XPATH, value=loc.BASKET_BUTTON
        ).text
        assert (button_before == BUTTON_TEXT_BEFORE and
                button_after == BUTTON_TEXT_AFTER)
    finally:
        driver.quit()


def test_sign_in_with_link_in_registration_form(driver, login, password):
    '''Вход в аккаунт по ссылке «Войти» формы регистрации.'''
    try:
        button_before = driver.find_element(
            by=By.XPATH, value=loc.ENTER_ACCOUNT_BUTTON
        ).text
        driver.find_element(
            by=By.XPATH, value=loc.ENTER_ACCOUNT_BUTTON
        ).click()
        driver.find_element(by=By.XPATH, value=loc.SIGN_UP_LINK).click()
        driver.find_element(by=By.XPATH, value=loc.SIGN_IN_LINK).click()
        sign_in_account(driver, login, password)
        button_after = driver.find_element(
            by=By.XPATH, value=loc.BASKET_BUTTON
        ).text
        assert (button_before == BUTTON_TEXT_BEFORE and
                button_after == BUTTON_TEXT_AFTER)
    finally:
        driver.quit()


def test_sign_in_with_link_in_restore_password_form(driver, login, password):
    '''Вход в аккаунт по ссылке «Войти» формы восстановления пароля.'''
    try:
        button_before = driver.find_element(
            by=By.XPATH, value=loc.ENTER_ACCOUNT_BUTTON
        ).text
        driver.find_element(
            by=By.XPATH, value=loc.ENTER_ACCOUNT_BUTTON
        ).click()
        driver.find_element(
            by=By.XPATH, value=loc.RESTORE_PASSWORD_LINK
        ).click()
        driver.find_element(
            by=By.XPATH, value=loc.REMEMBER_PASSWORD_SIGN_IN_LINK
        ).click()
        sign_in_account(driver, login, password)
        button_after = driver.find_element(
            by=By.XPATH, value=loc.BASKET_BUTTON
        ).text
        assert (button_before == BUTTON_TEXT_BEFORE and
                button_after == BUTTON_TEXT_AFTER)
    finally:
        driver.quit()
