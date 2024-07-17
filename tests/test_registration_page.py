import random
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from Locators import Locators

fake = Faker()


class TestRegistrationPage:
    def test_successful_registration(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')

        name = fake.first_name() + str(random.randint(100, 10000))
        email = fake.email() + str(random.randint(100, 10000))
        password = fake.password()

        driver.find_element(*Locators.INPUT_NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains('https://stellarburgers.nomoreparties.site/login'))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*Locators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains('https://stellarburgers.nomoreparties.site/account/profile'))

        input_name = driver.find_element(*Locators.INPUT_NAME)
        assert input_name.get_attribute('value') == name
        input_email = driver.find_element(*Locators.LOGIN_INPUT)
        assert input_email.get_attribute('value') == email

        driver.quit()

    def test_unsuccessful_registration_with_wrong_password(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')

        name = fake.first_name() + str(random.randint(100, 10000))
        email = fake.email() + str(random.randint(100, 10000))
        password = fake.password(length=5)

        driver.find_element(*Locators.INPUT_NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        input_error = driver.find_element(*Locators.INPUT_ERROR)
        assert input_error.text == 'Некорректный пароль'

        driver.quit()
