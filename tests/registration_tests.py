from selenium.webdriver.common.by import By

from . import locators as loc

USER_NAME = 'Пользователь'


def test_sign_up_with_log_in_button_account_created(driver, login, password):
    '''Успешная регистрация нового пользователя с использованием кнопки
    «Войти в аккаунт».'''
    find_element_args = (
        # кнопка «Войти в аккаунт»
        (By.XPATH, loc.ENTER_ACCOUNT_BTN, 'click', None),
        # ссылка зарегистрироваться
        (By.LINK_TEXT, loc.SIGN_UP_LINK_TEXT, 'click', None),
        # поле ввода имени формы регистрации
        (By.XPATH, loc.SIGN_UP_NAME_INPUT, 'send_keys', USER_NAME),
        # поле ввода email формы регистрации
        (By.XPATH, loc.SIGN_UP_EMAIL_INPUT, 'send_keys', login),
        # поле ввода пароля формы регистрации
        (By.XPATH, loc.SIGN_UP_PASSWORD_INPUT, 'send_keys', password),
        # кнопка «Зарегистрироваться»
        (By.XPATH, loc.SIGN_UP_BTN, 'click', None),
        # поле ввода логина формы «Вход»
        (By.XPATH, loc.SIGN_IN_EMAIL_INPUT, 'send_keys', login),
        # поле ввода пароля формы «Вход»
        (By.XPATH, loc.SIGN_IN_PASSWORD_INPUT, 'send_keys', password),
        # кнопка «Войти»
        (By.XPATH, loc.LOG_IN_BTN, 'click', None),
        # ссылка «Личный кабинет»
        (By.XPATH, loc.ACCOUNT_LINK, 'click', None),
        # ссылка «Профиль»
        (By.LINK_TEXT, loc.PROFILE_LINK_TEXT, 'click', None),
    )
    for by, value, method, text in find_element_args:
        if text is None:
            getattr(driver.find_element(by=by, value=value), method)()
        else:
            getattr(driver.find_element(by=by, value=value), method)(text)
    checks = (loc.PROFILE_NAME, USER_NAME), (loc.PROFILE_LOGIN, login)
    for value, expected in checks:
        assert (
            driver.find_element(by=By.XPATH, value=value).
            get_attribute(name='value') == expected
        )
    driver.quit()


def test_sign_up_with_account_link_account_created(driver, login, password):
    '''Успешная регистрация нового пользователя с использованием кнопки
    «Личный кабинет».'''
    driver.find_element(by=By.XPATH, value=loc.ACCOUNT_LINK).click()
    driver.find_element(by=By.LINK_TEXT, value=loc.SIGN_UP_LINK_TEXT).click()
    driver.find_element(by=By.XPATH, value=loc.SIGN_UP_NAME_INPUT).send_keys(USER_NAME)
    driver.find_element(by=By.XPATH, value=loc.SIGN_UP_EMAIL_INPUT).send_keys(login)
    driver.find_element(by=By.XPATH, value=loc.SIGN_UP_PASSWORD_INPUT).send_keys(password)
    driver.find_element(by=By.XPATH, value=loc.SIGN_UP_BTN).click()
    driver.find_element(by=By.XPATH, value=loc.SIGN_IN_EMAIL_INPUT).send_keys(login)
    driver.find_element(by=By.XPATH, value=loc.SIGN_IN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(by=By.XPATH, value=loc.LOG_IN_BTN).click()
    driver.find_element(by=By.XPATH, value=loc.ACCOUNT_LINK).click()
    driver.find_element(by=By.LINK_TEXT, value=loc.PROFILE_LINK_TEXT).click()
    profile_name = driver.find_element(by=By.XPATH, value=loc.PROFILE_NAME)
    assert profile_name.get_attribute(name='value') == USER_NAME
    profile_login = driver.find_element(by=By.XPATH, value=loc.PROFILE_LOGIN)
    assert profile_login.get_attribute(name='value') == login
    driver.quit()


def test_sign_up_with_invalid_password_shows_warning(driver):
    '''При попытке зарегистрировать пользователя с недопустимым паролем
    появляется предупреждающее сообщение.'''
    find_element_args = (
        (By.XPATH, loc.ACCOUNT_LINK, 'click', None),
        (By.LINK_TEXT, loc.SIGN_UP_LINK_TEXT, 'click', None),
        (By.XPATH, loc.SIGN_UP_PASSWORD_INPUT, 'send_keys', '1'),
        (By.XPATH, loc.SIGN_UP_BTN, 'click', None),
    )
    for by, value, method, text in find_element_args:
        if text is None:
            getattr(driver.find_element(by=by, value=value), method)()
        else:
            getattr(driver.find_element(by=by, value=value), method)(text)
    assert (
        driver.find_element(by=By.XPATH, value=loc.INVALID_PASSWORD_WARNING).
        text == 'Некорректный пароль'
    )
    driver.quit()
