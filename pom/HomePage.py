from typing import List
from selenium.webdriver.common.by import By
from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from base.utils import Utils


class HomePage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__NAV_LINKS = 'div.leftColumn > ul > li > a'
        self.NAV_LINK_TEXT = 'Главная,О магазине,Гарантия,Доставка,Кредит,Онлайн кредит,FAQ,Контакты,O!'
        self.__CATALOG_PRODUCT = '#leftMenu > li'
        self.CATALOG_EXPECTED_TEXT_PRODUCT = \
            'Мобильные телефоны,Устройства О!,Аксессуары,Сумки,Часы,SIM-карты O!,Гаджеты,Электросамокаты'
        self.__SEARCH_WRITE = '#topSearchLine > div:nth-child(1) > form:nth-child(1)' \
                            ' > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)'
        self.__CLICK_SEARCH = '#topSearchLine > div:nth-child(1) > form:nth-child(1) > div:nth-child(1)' \
                            ' > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)'

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__NAV_LINKS, 'Header Navigation Links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return Utils.join_strings(nav_links_text)

    def get_nav_link_by_name(self, name) -> WebElement:
        elements = self.get_nav_links()
        return self.get_elemet_by_text(elements, name)

    def get_catalog_product(self) -> List[WebElement]:
        return self.are_visible('css', self.__CATALOG_PRODUCT, 'Header Navigation Links')

    def get_catalog_product_text(self) -> str:
        catalog_products = self.get_catalog_product()
        catalog_products_text = self.get_text_from_webelements(catalog_products)
        return Utils.join_strings(catalog_products_text)

    def get_catalog_by_name(self, name) -> WebElement:
        elements = self.get_catalog_product()
        return self.get_elemet_by_text(elements, name)

    def write_search(self):
        return self.is_visible('css', self.__SEARCH_WRITE, 'error element')

    def click_search(self):
        return self.is_visible('css', self.__CLICK_SEARCH, 'error element')

    def write_search_click_and_clear(self, text):
        element = self.write_search()
        return self.send_keys_custom(element, text)
