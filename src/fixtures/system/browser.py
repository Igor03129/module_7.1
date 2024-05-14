import logging

from allure_commons._allure import step
from selenium.webdriver import Remote
import pytest

from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='class')
def selenium(pytestconfig):

    options = Options()
    browser_name = pytestconfig.getini("browser_name")
    logging.info(f'Prepare {browser_name} browser...')

    if pytestconfig.getini("headless") == "True" and browser_name == "chrome":
        options.add_argument("--headless")
    options.page_load_strategy = 'eager'
    options.add_argument("--window-size=1920,1080")
    with step('Запуск браузера'):
        driver = Remote(
            desired_capabilities={
                "browserName": pytestconfig.getini("browser_name"),
                 "browserVersion": pytestconfig.getini("browser_version")
             },
             command_executor=pytestconfig.getini("selenium_url"),
             options=options
        )
    logging.info(f'Browser {browser_name} has been started.')
    yield driver
    logging.info(f'Close {browser_name} browser...')
    driver.quit()
