'''Тесты для проверки функциональности регистрации нового пользователя
web-сервиса «Stellar Burgers».'''
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import INVALID_PASSWORD, USER_NAME, WARNING
from tests.locators import Locators as loc


class TestRegistration:

    def test_sign_up_new_account_created(
            self, driver, generate_login, generate_password
          ):
        '''Успешная регистрация нового пользователя.'''
        driver.find_element(*loc.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*loc.SIGN_UP_LINK).click()
        driver.find_element(*loc.SIGN_UP_NAME_INPUT).send_keys(USER_NAME)
        driver.find_element(*loc.SIGN_UP_EMAIL_INPUT).send_keys(
            generate_login
        )
        driver.find_element(*loc.SIGN_UP_PASSWORD_INPUT).send_keys(
            generate_password
        )
        driver.find_element(*loc.SIGN_UP_BUTTON).click()
        driver.find_element(*loc.ACCOUNT_LINK).click()
        driver.find_element(*loc.SIGN_IN_EMAIL_INPUT).send_keys(
            generate_login
        )
        driver.find_element(*loc.SIGN_IN_PASSWORD_INPUT).send_keys(
            generate_password
        )
        driver.find_element(*loc.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(loc.BASKET_BUTTON)
        )
        driver.find_element(*loc.ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                loc.PROFILE_LINK
            )
        )
        driver.find_element(*loc.PROFILE_LINK).click()
        assert (
            driver.find_element(*loc.PROFILE_NAME).get_attribute(name='value')
            == USER_NAME and
            driver.find_element(*loc.PROFILE_LOGIN).get_attribute(name='value')
            == generate_login
        )

    def test_sign_up_with_invalid_password_warning(self, driver):
        '''Предупреждающее сообщение о недопустимом пароле при регистрации
        пользователя.'''
        driver.find_element(*loc.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*loc.SIGN_UP_LINK).click()
        driver.find_element(*loc.SIGN_UP_PASSWORD_INPUT).send_keys(
            INVALID_PASSWORD
        )
        driver.find_element(*loc.SIGN_UP_BUTTON).click()
        assert driver.find_element(
            *loc.INVALID_PASSWORD_WARNING
        ).text == WARNING
