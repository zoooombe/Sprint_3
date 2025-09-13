import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.locators import *


class TestConstructor:
    def test_navigate_to_buns_section(self, driver):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(SAUCES_SECTION)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(ACTIVE_SECTION, "Соусы")
        )

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(BUNS_SECTION)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(ACTIVE_SECTION, "Булки")
        )

        active_section = driver.find_element(*ACTIVE_SECTION)
        assert "Булки" in active_section.text

    def test_navigate_to_sauces_section(self, driver):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(SAUCES_SECTION)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(ACTIVE_SECTION, "Соусы")
        )

        active_section = driver.find_element(*ACTIVE_SECTION)
        assert "Соусы" in active_section.text

    def test_navigate_to_fillings_section(self, driver):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(FILLINGS_SECTION)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(ACTIVE_SECTION, "Начинки")
        )

        active_section = driver.find_element(*ACTIVE_SECTION)
        assert "Начинки" in active_section.text