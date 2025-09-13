import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")  # Отключаем GPU
        options.add_argument("--disable-extensions")  # Отключаем расширения
        options.add_argument("--disable-infobars")  # Отключаем информационные панели
        options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Отключаем автоматизацию
        options.add_experimental_option('useAutomationExtension', False)  # Отключаем автоматизацию
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")

    driver.get("https://stellarburgers.nomoreparties.site/")

    yield driver

    driver.quit()