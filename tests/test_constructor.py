'''Тесты для проверки функциональности перехода между категориями
в конструкторе web-сервиса «Stellar Burgers».'''
from data import ACTIVE
from tests.locators import Locators as loc


class TestConstructor:

    def test_switch_to_buns_in_constructor(sel, driver):
        '''Переход к категории «Булки» в конструкторе.'''
        driver.find_element(*loc.SAUCES).click()
        buns_elem = driver.find_element(*loc.BUNS)
        buns_elem.click()
        toppings_elem = driver.find_element(*loc.TOPPINGS)
        sauces_elem = driver.find_element(*loc.SAUCES)
        assert (
            ACTIVE in buns_elem.get_attribute(name='class') and
            ACTIVE not in toppings_elem.get_attribute(name='class') and
            ACTIVE not in sauces_elem.get_attribute(name='class')
        )

    def test_switch_to_sauces_in_constructor(self, driver):
        '''Переход к категории «Соусы» в конструкторе.'''
        sauces_elem = driver.find_element(*loc.SAUCES)
        sauces_elem.click()
        buns_elem = driver.find_element(*loc.BUNS)
        toppings_elem = driver.find_element(*loc.TOPPINGS)
        assert (
            ACTIVE in sauces_elem.get_attribute(name='class') and
            ACTIVE not in buns_elem.get_attribute(name='class') and
            ACTIVE not in toppings_elem.get_attribute(name='class')
        )

    def test_switch_to_toppings_in_constructor(self, driver):
        '''Переход к категории «Начинки» в конструкторе.'''
        toppings_elem = driver.find_element(*loc.TOPPINGS)
        toppings_elem.click()
        buns_elem = driver.find_element(*loc.BUNS)
        sauces_elem = driver.find_element(*loc.SAUCES)
        assert (
            ACTIVE in toppings_elem.get_attribute(name='class') and
            ACTIVE not in buns_elem.get_attribute(name='class') and
            ACTIVE not in sauces_elem.get_attribute(name='class')
        )
