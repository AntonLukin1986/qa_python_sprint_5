import sys
from pprint import pprint
from types import ModuleType

from tests import (
    constructor_tests, personal_account_tests, registration_tests,
    sign_in_tests
)

from tools import (
    chrome_driver_init, create_account, generate_login, generate_password
)

namespace = globals()


def test_kit():
    '''Получить набор всех импортированных тестов в виде словаря, где:
    ключ - имя тестового модуля, значение - список тестов в модуле.'''
    imported_test_modules = [
        key for key, value in namespace.items()
        if key.endswith('tests') and isinstance(value, ModuleType)
    ]
    kit = dict()
    for module in imported_test_modules:
        tests = [
            name for name in dir(namespace[module])
            if name.startswith('test')
        ]
        kit[module] = tests
    return kit


def run_all_tests(kit, test_suite):
    '''Запуск всех тестов.'''
    print('\nЗапуск всех тестов...')
    for module, tests in kit.items():
        for test in tests:
            current_test(module, test, **test_suite)


def run_partial_tests(kit, partial, test_suite):
    '''Выборочный запуск тестов и/или тестовых модулей.'''
    for name in partial:
        found = False
        for module, tests in kit.items():
            if name != module and name not in tests:
                continue
            found = True
            if name == module:
                print(f'\nЗапуск тестового модуля {name.upper()}...')
                for test in tests:
                    current_test(name, test, **test_suite)
            else:
                current_test(module, name, **test_suite)
            break
        if not found:
            print(f'«{name}» не обнаружен среди импортированных тестов!')


def current_test(module, test, *, driver, hide, login, password):
    '''Запуск текущего теста.'''
    print(f'\n>>> {test}    (модуль {module})')
    driver = driver(hide)
    getattr(namespace[module], test)(driver, login, password)


def unify_partial(partial):
    '''Проверка корректности и унификация аргумента «partial».'''
    if not partial:
        return partial
    if not isinstance(partial, str | tuple | list):
        print('Аргумент «partial» ожидает строку, кортеж или список с именами '
              'тестов и/или тестовых модулей!')
        sys.exit()
    if isinstance(partial, str):
        partial = (partial,)
    return partial


def main(hide: bool = True,
         partial: bool | str | tuple[str, ...] | list[str] = False,
         show_tests: bool = False):
    '''Управление запуском тестов. Параметры:
    hide - выполнять в фоновом режиме
    partial - выборочные тесты: имена тестов и/или тестовых модулей
    show_tests - отобразить набор всех импортированных тестов без их запуска
    '''
    kit = test_kit()
    if show_tests:
        return pprint(kit)
    test_suite = {
        'driver': chrome_driver_init,
        'hide': hide,
        'login': generate_login(),
        'password': generate_password()
    }
    partial = unify_partial(partial)
    create_account(**test_suite)
    if not partial:
        run_all_tests(kit, test_suite)
    else:
        run_partial_tests(kit, partial, test_suite)


if __name__ == '__main__':
    main(hide=True, partial=False, show_tests=False)
