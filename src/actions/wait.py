import allure
import pytest



@pytest.fixture
def wait_element(selenium):
    @allure.step('Ожидание элимента {url}')
    def callback(by, value):
        selenium.get(url)
    return callback