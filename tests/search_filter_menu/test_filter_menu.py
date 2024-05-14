import pytest
from allure_commons._allure import step

class TestFilterMenu:
    @pytest.mark.parametrize('profession_name,filter_names', [
        ("Программирование", ["Все программы", "Бэкенд-разработка", "Веб-разработка", "Мобильная разработка", "Анализ данных", "IT-инфраструктура"]),
        ("Дизайн", ["Все программы", "Цифровой дизайн", "Дизайн среды", "Мода и фотография"]),
        ("Маркетинг", ["Все программы", "Бренд-маркетинг", "Аналитика", "Перформанс-маркетинг", "Электронная комерция"]),
    ])
    def test_list_filter_block(self, profession_name, filter_names, wait_element, go_to_url, page):
        go_to_url('https://skillbox.ru/courses/')

        with step(f'Выбор фильтра курсов {profession_name}'):
            wait_element(f"text={profession_name}").click()

        wait_element('.filter-block__direction')
        filter_blocks = page.query_selector_all('.filter-block__direction > a')

        with step('Проверка кнопки фильтрации'):
            for actual_filter, expected_filter in zip(filter_blocks, filter_names):
                with step(f'Сравнение текущего текста "{actual_filter.inner_text()}"с ожидаемым {expected_filter}'):
                    assert actual_filter.inner_text() == expected_filter
