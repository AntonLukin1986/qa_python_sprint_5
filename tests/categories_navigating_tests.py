'''Тесты для проверки функциональности перехода между категориями
в конструкторе.'''
from selenium.webdriver.common.by import By

from . import locators as loc

ACTIVE = 'current'


def test_switch_to_buns_in_constructor(driver):
    '''Переход к категории «Булки» в конструкторе.'''
    driver.find_element(by=By.XPATH, value=loc.SAUCES).click()
    buns_elem = driver.find_element(by=By.XPATH, value=loc.BUNS)
    buns_elem.click()
    toppings_elem = driver.find_element(by=By.XPATH, value=loc.TOPPINGS)
    sauces_elem = driver.find_element(by=By.XPATH, value=loc.SAUCES)
    assert (ACTIVE in buns_elem.get_attribute(name='class') and
            ACTIVE not in toppings_elem.get_attribute(name='class') and
            ACTIVE not in sauces_elem.get_attribute(name='class'))
    driver.quit()


def test_switch_to_sauces_in_constructor(driver):
    '''Переход к категории «Соусы» в конструкторе.'''
    sauces_elem = driver.find_element(by=By.XPATH, value=loc.SAUCES)
    sauces_elem.click()
    buns_elem = driver.find_element(by=By.XPATH, value=loc.BUNS)
    toppings_elem = driver.find_element(by=By.XPATH, value=loc.TOPPINGS)
    assert (ACTIVE in sauces_elem.get_attribute(name='class') and
            ACTIVE not in buns_elem.get_attribute(name='class') and
            ACTIVE not in toppings_elem.get_attribute(name='class'))
    driver.quit()


def test_switch_to_toppings_in_constructor(driver):
    '''Переход к категории «Начинки» в конструкторе.'''
    toppings_elem = driver.find_element(by=By.XPATH, value=loc.TOPPINGS)
    toppings_elem.click()
    buns_elem = driver.find_element(by=By.XPATH, value=loc.BUNS)
    sauces_elem = driver.find_element(by=By.XPATH, value=loc.SAUCES)
    assert (ACTIVE in toppings_elem.get_attribute(name='class') and
            ACTIVE not in buns_elem.get_attribute(name='class') and
            ACTIVE not in sauces_elem.get_attribute(name='class'))
    driver.quit()
