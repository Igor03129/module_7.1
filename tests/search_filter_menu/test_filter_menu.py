from selenium.webdriver.common.by import By
import pytest

class TestFilterMenu:
    @pytest.mark.parametrize('profession_name,filter_names', [
        ("Программирование", ["Все программы", "Бэкенд-разработка", "Веб-разработка", "Мобильная разработка", "Анализ данных", "IT-инфраструктура"]),
        ("Дизайн", ["Все программы", "Цифровой дизайн", "Дизайн среды", "Мода и фотография"]),
        ("Маркетинг", ["Все программы", "Бренд-маркетинг", "Аналитика", "Перформанс-маркетинг", "Электронная комерция"]),
    ])
    def test_list_filter_block(self, profession_name, filter_names, selenium):
        selenium.get('https://skillbox.ru/courses/')
        selenium.find_element(By.LINK_TEXT, profession_name).click()
        filter_blocks = selenium.find_element(By.CSS_SELECTOR, '.filter-block__direction')\
            .find_elements(By.CSS_SELECTOR, 'a')

        for actual_filter, expected_filter in zip(filter_blocks, filter_names):
            assert actual_filter.text == expected_filter
        assert True
