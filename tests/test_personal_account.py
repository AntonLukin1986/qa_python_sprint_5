'''Тесты для проверки функциональности личного кабинета web-сервиса
«Stellar Burgers».'''
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import Locators as loc


class TestPersonalAccount:

    def test_enter_account_with_account_link(
            self, driver, log_in, personal_account_text
          ):
        '''Вход в личный кабинет по ссылке «Личный кабинет».'''
        try:
            driver.find_element(*loc.ACCOUNT_LINK).click()
            WebDriverWait(driver, 5).until(
                expected_conditions.presence_of_element_located(
                    loc.PERSONAL_ACCOUNT
                )
            )
            assert (
                driver.find_element(*loc.PERSONAL_ACCOUNT).text ==
                personal_account_text
            )
        finally:
            driver.quit()

    def test_switch_from_account_with_constructor_link(
            self, driver, log_in, constructor_header
          ):
        '''Переход из личного кабинета по клику на ссылку «Конструктор».'''
        try:
            driver.find_element(*loc.ACCOUNT_LINK).click()
            driver.find_element(*loc.CONSTRUCTOR_LINK).click()
            assert (
                driver.find_element(*loc.CONSTRUCT_BURGER).text ==
                constructor_header
            )
        finally:
            driver.quit()

    def test_switch_from_account_with_logo_link(
            self, driver, log_in, constructor_header
          ):
        '''Переход из личного кабинета по клику на логотип
        «Stellar Burgers».'''
        try:
            driver.find_element(*loc.ACCOUNT_LINK).click()
            driver.find_element(*loc.LOGO_LINK).click()
            assert (
                driver.find_element(*loc.CONSTRUCT_BURGER).text ==
                constructor_header
            )
        finally:
            driver.quit()

    def test_log_out_from_account_with_exit_button(
            self, driver, log_in, sign_in_form_title
          ):
        '''Выход из личного кабинета по кнопке «Выйти».'''
        try:
            driver.find_element(*loc.ACCOUNT_LINK).click()
            WebDriverWait(driver, 5).until(
                expected_conditions.presence_of_element_located(
                    loc.EXIT_BUTTON
                )
            )
            driver.find_element(*loc.EXIT_BUTTON).click()
            WebDriverWait(driver, 5).until(
                expected_conditions.presence_of_element_located(
                    loc.SIGN_IN_FORM
                )
            )
            assert (
                driver.find_element(*loc.SIGN_IN_FORM).text ==
                sign_in_form_title
            )
        finally:
            driver.quit()
