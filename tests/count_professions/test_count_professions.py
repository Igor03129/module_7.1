import pytest
from allure_commons._allure import step
from playwright.sync_api import ElementHandle


class TestCountProfessions:
    @pytest.fixture
    def setup_count_profession_test(self, go_to_url, wait_element) -> ElementHandle:
        go_to_url('https://skillbox.ru/')

        with step("Переход в блок профессии"):
            wait_element('//h3[contains(text(), "Профессии")]/following-sibking::a/span').click()

        return wait_element('.courses-block > .courses-block__load')


    def test_default_count(self, setup_count_profession_test):

        actual_text = setup_count_profession_test.inner_text()
        expected_text = 'Ещё 10 профессий из 89'
        with step(f'Проверка, что в кнопке загрузки содержится текст "{expected_text}"'):
            assert expected_text in actual_text

    def test_count_after_load_additional_professions(self, setup_count_profession_test, wait_element):
        default_count_button = setup_count_profession_test
        expected_text = 'Ещё 10 профессий из 79'
        with step('Загрузка второй страницы'):
            default_count_button.click()

        wait_element(f"//*[contains(@class, 'courses-block')]/*[contains(@class, 'courses-block__load')]"
                     f"[contains(text(), '{expected_text}')]")
 # f'.//courses-block/button[contains(text(), {expected_text})]'