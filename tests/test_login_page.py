from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Locators import Locators


class TestLoginPage:
    def test_login_from_main_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')

        email = 'elenaviushkova11_333@yandex.ru'
        password = '1111111'

        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*Locators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains('https://stellarburgers.nomoreparties.site/account/profile'))

        input_email = driver.find_element(*Locators.LOGIN_INPUT)
        assert input_email.get_attribute('value') == email

        driver.quit()

    def test_login_from_personal_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')

        email = 'elenaviushkova11_333@yandex.ru'
        password = '1111111'

        driver.find_element(*Locators.ACCOUNT_LINK).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*Locators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains('https://stellarburgers.nomoreparties.site/account/profile'))

        input_email = driver.find_element(*Locators.LOGIN_INPUT)
        assert input_email.get_attribute('value') == email

        driver.quit()

    def test_login_from_registration_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')

        email = 'elenaviushkova11_333@yandex.ru'
        password = '1111111'

        driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION_AND_FORGOT_PASSWORD_PAGE).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*Locators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains('https://stellarburgers.nomoreparties.site/account/profile'))

        input_email = driver.find_element(*Locators.LOGIN_INPUT)
        assert input_email.get_attribute('value') == email

        driver.quit()

    def test_login_from_forgot_password_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')

        email = 'elenaviushkova11_333@yandex.ru'
        password = '1111111'

        driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION_AND_FORGOT_PASSWORD_PAGE).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*Locators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains('https://stellarburgers.nomoreparties.site/account/profile'))

        input_email = driver.find_element(*Locators.LOGIN_INPUT)
        assert input_email.get_attribute('value') == email

        driver.quit()

