'''Тесты для проверки функциональности входа в аккаунт web-сервиса
«Stellar Burgers».'''
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import EMAIL, PASSWORD
from tests.locators import Locators as loc


class TestSignIn:

    def button_after_log_in(self, driver):
        '''Аутентификация пользователя и получение текста кнопки
        «Оформить заказ».'''
        driver.find_element(*loc.SIGN_IN_EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*loc.SIGN_IN_PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*loc.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(loc.BASKET_BUTTON)
        )
        return driver.find_element(*loc.BASKET_BUTTON).text

    def test_sign_in_with_enter_account_button(self, driver):
        '''Вход в аккаунт по кнопке «Войти в аккаунт» на главной странице.'''
        enter_account_btn = driver.find_element(*loc.ENTER_ACCOUNT_BUTTON)
        button_before = enter_account_btn.text
        enter_account_btn.click()
        assert (
            button_before !=
            self.button_after_log_in(driver)
        )

    def test_sign_in_with_account_link(self, driver):
        '''Вход в аккаунт по ссылке «Личный кабинет».'''
        button_before = driver.find_element(*loc.ENTER_ACCOUNT_BUTTON).text
        driver.find_element(*loc.ACCOUNT_LINK).click()
        assert (
            button_before !=
            self.button_after_log_in(driver)
        )

    def test_sign_in_with_link_in_registration_form(self, driver):
        '''Вход в аккаунт по ссылке «Войти» формы регистрации.'''
        enter_account_btn = driver.find_element(*loc.ENTER_ACCOUNT_BUTTON)
        button_before = enter_account_btn.text
        enter_account_btn.click()
        driver.find_element(*loc.SIGN_UP_LINK).click()
        driver.find_element(*loc.SIGN_IN_LINK).click()
        assert (
            button_before !=
            self.button_after_log_in(driver)
        )

    def test_sign_in_with_link_in_restore_password_form(self, driver):
        '''Вход в аккаунт по ссылке «Войти» формы восстановления пароля.'''
        enter_account_btn = driver.find_element(*loc.ENTER_ACCOUNT_BUTTON)
        button_before = enter_account_btn.text
        enter_account_btn.click()
        driver.find_element(*loc.RESTORE_PASSWORD_LINK).click()
        driver.find_element(*loc.REMEMBER_PASSWORD_SIGN_IN_LINK).click()
        assert (
            button_before !=
            self.button_after_log_in(driver)
        )
