import time
import pytest
from pom.HomePage import HomePage


@pytest.mark.usefixtures('setup')
class TestHomePage:

    @pytest.mark.skip
    def test_nav_links_text(self):
        home_page_nav = HomePage(self.driver)
        actual_links = home_page_nav.get_nav_links_text()
        expected_links = home_page_nav.NAV_LINK_TEXT
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
        expected_links = home_page_nav.CATALOG_EXPECTED_TEXT_PRODUCT
        assert actual_catalog_products == expected_links, f"\nВЕРНУЛ: \n {actual_catalog_products}"

    def test_click_catalog_product(self):
        home_page_nav = HomePage(self.driver)
        home_page_nav.get_catalog_product()[0].click()
        time.sleep(2)
