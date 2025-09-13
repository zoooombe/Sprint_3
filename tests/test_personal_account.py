import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.locators import *
from utils.generate_data import generate_email, generate_password, generate_name


class TestPersonalAccount:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.name = generate_name()
        self.email = generate_email()
        self.password = generate_password()

        driver.find_element(*LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(REGISTER_LINK)).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(REGISTER_NAME_INPUT)).send_keys(self.name)
        driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(self.email)
        driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys(self.password)
        driver.find_element(*REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_HEADER))
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(self.email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(self.password)
        driver.find_element(*LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON))

        yield

    def test_navigate_to_personal_account(self, driver):
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PROFILE_LINK))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    def test_navigate_from_personal_account_to_constructor_via_button(self, driver):
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PROFILE_LINK))

        driver.find_element(*CONSTRUCTOR_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_navigate_from_personal_account_to_constructor_via_logo(self, driver):
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PROFILE_LINK))

        driver.find_element(*LOGO).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"