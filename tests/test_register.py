import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.locators import *
from utils.generate_data import generate_email, generate_password, generate_name


class TestRegister:
    @pytest.mark.parametrize("name, email, password", [
        (generate_name(), generate_email(), generate_password()),
        (generate_name(), generate_email(), generate_password(10)),
    ])
    def test_successful_registration(self, driver, name, email, password):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LOGIN_BUTTON_MAIN)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(REGISTER_LINK)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(REGISTER_NAME_INPUT)
        ).send_keys(name)

        driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(email)
        driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys(password)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(REGISTER_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LOGIN_BUTTON)
        )
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_registration_with_invalid_password(self, driver):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LOGIN_BUTTON_MAIN)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(REGISTER_LINK)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(REGISTER_NAME_INPUT)
        ).send_keys(generate_name())

        driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys("123")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(REGISTER_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ERROR_MESSAGE)
        )

        error_message = driver.find_element(*ERROR_MESSAGE).text
        assert "Некорректный пароль" in error_message or "пароль" in error_message.lower()