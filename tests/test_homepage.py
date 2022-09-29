import time

import pytest
from pom.HomePage import HomePage


@pytest.mark.usefixtures('setup')
class TestHomePage:

    @pytest.mark.skip
    def test_nav_links_text(self):
        home_page_nav = HomePage(self.driver)
        actual_links = home_page_nav.get_nav_links_text()
        expected_links = home_page_nav.EXPECTED_NAV_LINK_TEXT
        assert actual_links == expected_links, f"\nВЕРНУЛ:\n {actual_links}"

    @pytest.mark.skip
    def test_click_nav_links(self):
        home_page_nav = HomePage(self.driver)
        for index in range(9):
            home_page_nav.get_nav_links()[index].click()

    @pytest.mark.skip
    def test_catalog_product_text(self):
        home_page_nav = HomePage(self.driver)
        actual_catalog_products = home_page_nav.get_catalog_product_text()
        expected_links = home_page_nav.EXPECTED_CATALOG_TEXT_PRODUCT
        assert actual_catalog_products == expected_links, f"\nВЕРНУЛ: \n {actual_catalog_products}"

    @pytest.mark.skip
    def test_click_catalog_product(self):
        home_page_nav = HomePage(self.driver)
        for index in range(8):
            home_page_nav.get_catalog_product()[index].click()
            home_page_nav.driver.back()

    @pytest.mark.skip
    def test_search_write(self):
        search_write = HomePage(self.driver)
        search_write.write_search_click_and_clear('часы')
        search_write.click_search().click()
        get_search_element = search_write.get_search_element().text
        assert get_search_element == search_write.EXPECTED_GET_SEARCH, f"ВЕРНУЛ: {get_search_element}"

    @pytest.mark.skip
    def test_language_choice(self):
        language = HomePage(self.driver)
        language.language_choice().click()
        get_language_element = language.get_language_element().text
        assert get_language_element == 'RU', f"ВЕРНУЛ: {get_language_element}"

    @pytest.mark.skip
    def test_catalog_type_text(self):
        catalog_type_text = HomePage(self.driver)
        result_catalog_type_text = catalog_type_text.catalog_type_get_text()
        assert result_catalog_type_text == catalog_type_text.EXPECTED_GET_CATALOG, f"ВЕРНУЛ: {result_catalog_type_text}"

    def test_catalog_type_click(self):
        catalog_type_click = HomePage(self.driver)
        for index in range(3):
            self.driver.execute_script("window.scrollBy(0, 150);")
            catalog_type_click.catalog_type()[index].click()
