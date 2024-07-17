from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Locators import Locators


class TestLogout:
    def test_logout(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')

        email = 'elenaviushkova11_333@yandex.ru'
        password = '1111111'

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*Locators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains('https://stellarburgers.nomoreparties.site/account/profile'))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains('https://stellarburgers.nomoreparties.site/login'))

        expected_url = 'https://stellarburgers.nomoreparties.site/login'
        assert driver.current_url == expected_url

        driver.quit()
