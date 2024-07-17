from Locators import Locators


class TestConstructorSection:
    def test_transition_between_sections(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')

        def click_element_with_js(locator):
            element = driver.find_element(*locator)
            driver.execute_script("arguments[0].scrollIntoView();", element)
            driver.execute_script("arguments[0].click();", element)

        click_element_with_js(Locators.SAUCES_TAB)
        sauces_tab = driver.find_element(*Locators.SAUCES_TAB)
        assert 'tab_tab_type_current__2BEPc' in sauces_tab.get_attribute(
            'class') and sauces_tab.text == "Соусы"

        click_element_with_js(Locators.FILLINGS_TAB)
        fillings_tab = driver.find_element(*Locators.FILLINGS_TAB)
        assert 'tab_tab_type_current__2BEPc' in fillings_tab.get_attribute(
            'class') and fillings_tab.text == "Начинки"

        click_element_with_js(Locators.BUNS_TAB)
        buns_tab = driver.find_element(*Locators.BUNS_TAB)
        assert 'tab_tab_type_current__2BEPc' in buns_tab.get_attribute('class') and buns_tab.text == "Булки"

        driver.quit()