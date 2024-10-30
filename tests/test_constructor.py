from tests.locators import Locators as loc


class TestConstructor:
    '''Тесты для проверки функциональности перехода между категориями
    в конструкторе web-сервиса «Stellar Burgers».'''
    def test_switch_to_buns_in_constructor(self, driver, active):
        '''Переход к категории «Булки» в конструкторе.'''
        try:
            driver.find_element(*loc.SAUCES).click()
            buns_elem = driver.find_element(*loc.BUNS)
            buns_elem.click()
            toppings_elem = driver.find_element(*loc.TOPPINGS)
            sauces_elem = driver.find_element(*loc.SAUCES)
            assert (
                active in buns_elem.get_attribute(name='class') and
                active not in toppings_elem.get_attribute(name='class') and
                active not in sauces_elem.get_attribute(name='class')
            )
        finally:
            driver.quit()

    def test_switch_to_sauces_in_constructor(self, driver, active):
        '''Переход к категории «Соусы» в конструкторе.'''
        try:
            sauces_elem = driver.find_element(*loc.SAUCES)
            sauces_elem.click()
            buns_elem = driver.find_element(*loc.BUNS)
            toppings_elem = driver.find_element(*loc.TOPPINGS)
            assert (
                active in sauces_elem.get_attribute(name='class') and
                active not in buns_elem.get_attribute(name='class') and
                active not in toppings_elem.get_attribute(name='class')
            )
        finally:
            driver.quit()

    def test_switch_to_toppings_in_constructor(self, driver, active):
        '''Переход к категории «Начинки» в конструкторе.'''
        try:
            toppings_elem = driver.find_element(*loc.TOPPINGS)
            toppings_elem.click()
            buns_elem = driver.find_element(*loc.BUNS)
            sauces_elem = driver.find_element(*loc.SAUCES)
            assert (
                active in toppings_elem.get_attribute(name='class') and
                active not in buns_elem.get_attribute(name='class') and
                active not in sauces_elem.get_attribute(name='class')
            )
        finally:
            driver.quit()
