import pytest
from allure_commons._allure import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestCountProfessions:
    @pytest.fixture
    def setup_count_profession_test(self, go_to_url, selenium):
        go_to_url('https://skillbox.ru/')

        with step("Переход в блок профессии"):
            blockProf = WebDriverWait(selenium, timeout=60).until(
                lambda driver: driver.find_element(By.XPATH, './/h2[contains(text(), "Профессии")]/following-sibling::a/span')
            )
            blockProf.click()
        with step('Ожидаем элимент с количеством профессий в странице'):
            actual_element = WebDriverWait(selenium, timeout=60).until(
                lambda driver: driver.find_element(By.CSS_SELECTOR, '.courses-block > button')
            )
        return actual_element


    def test_default_count(self, setup_count_profession_test):

        actual_text = setup_count_profession_test.text
        expected_text = 'Ещё 10 профессий из 89'
        assert expected_text in actual_text

    def test_count_after_load_additional_professions(self, setup_count_profession_test, selenium):
        default_count_button = setup_count_profession_test
        expected_text = 'Ещё 10 профессий из 79'
        default_count_button.click()

        actual_element = WebDriverWait(selenium, timeout=60).until(
            lambda driver: driver.find_element(
                By.XPATH,
                f'.//courses-block/button[contains(text(), {expected_text})]'
            )
        )
