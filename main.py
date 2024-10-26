import random
import string

from selenium import webdriver

from tests.registration_tests import *
from tests.sing_in_tests import *
from tests.personal_account_tests import *
from tests.categories_navigating_tests import *



HOME_URL = 'https://stellarburgers.nomoreparties.site/'       ##########################################################################


def generate_password():
    '''Генератор паролей.'''
    length = random.randint(6, 10)
    chars = string.digits + string.ascii_letters + string.punctuation
    return ''.join(random.choices(chars, k=length))


def generate_login():
    '''Генератор логинов.'''
    prefix = {
        'chars': string.digits + string.ascii_lowercase,
        'min_max_len': (3, 10),
        'sep': '@'
    }
    domain = {
        'chars': string.ascii_lowercase,
        'min_max_len': (2, 7),
        'sep': '.'
    }
    zone = {
        'chars': string.ascii_lowercase,
        'min_max_len': (2, 3),
        'sep': ''
    }
    login = ''
    for segment in prefix, domain, zone:
        chars = segment['chars']
        length = random.randint(*segment['min_max_len'])
        login += ''.join(random.choices(chars, k=length)) + segment['sep']
    return login


def chrome_driver_init(hide):
    '''Создаёт драйвер браузера Google Chrome, открывает страницу проекта.'''
    options = webdriver.ChromeOptions()
    options.add_argument(argument='--headless' if hide else 'start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(time_to_wait=5)
    driver.get(url=HOME_URL)
    return driver


def main(hide=False):
    '''Запуск всех тестов.'''
    test_sign_up_new_account_created(chrome_driver_init(hide), generate_login(), generate_password())
    test_sign_up_with_invalid_password_warning(chrome_driver_init(hide))

    test_sign_in_with_enter_account_button(chrome_driver_init(hide), generate_login(), generate_password())
    test_sign_in_with_account_link(chrome_driver_init(hide), generate_login(), generate_password())
    test_sign_in_with_link_in_registration_form(chrome_driver_init(hide), generate_login(), generate_password())
    test_sign_in_with_link_in_restore_password_form(chrome_driver_init(hide), generate_login(), generate_password())

    test_enter_account_with_account_link(chrome_driver_init(hide), generate_login(), generate_password())
    test_switch_from_account_with_constructor_link(chrome_driver_init(hide), generate_login(), generate_password())
    test_switch_from_account_with_logo_link(chrome_driver_init(hide), generate_login(), generate_password())
    test_log_out_from_account_with_exit_button(chrome_driver_init(hide), generate_login(), generate_password())

    test_switch_to_buns_in_constructor(chrome_driver_init(hide))
    test_switch_to_sauces_in_constructor(chrome_driver_init(hide))
    test_switch_to_toppings_in_constructor(chrome_driver_init(hide))


if __name__ == '__main__':
    main(hide=True)
    #print(generate_login())
    #print(generate_password())
