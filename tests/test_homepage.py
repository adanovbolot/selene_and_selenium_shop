import time
import pytest
from pom.HomePage import HomePage


@pytest.mark.usefixtures('setup')
class TestHomePage:

    def test_nav_links(self):
        home_page_nav = HomePage(self.driver)
        actual_links = home_page_nav.get_nav_links_text()
        expected_links = home_page_nav.NAV_LINK_TEXT
        assert actual_links == expected_links, f"\nВЕРНУЛ:\n {actual_links}"
        for indx in range(9):
            home_page_nav.get_nav_links()[indx].click()

