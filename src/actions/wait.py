import allure
import pytest
from selenium.webdriver.common.devtools.v122 import page


@pytest.fixture
def wait_element(selenium):
    @allure.step('Ожидание элимента со значением {value}')
    def callback(value):
        return page.wait_for_selector(value)
    return callback