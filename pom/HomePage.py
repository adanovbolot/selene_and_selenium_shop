from typing import List
import allure
from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from base.utils import Utils


class HomePage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        #LOCATOR
        self.__NAV_LINKS = 'div.leftColumn > ul > li > a'
        self.__CATALOG_PRODUCT = '#leftMenu > li'
        self.__SEARCH_WRITE = '#topSearchLine > div:nth-child(1) > form:nth-child(1)' \
                            ' > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)'
        self.__CLICK_SEARCH = '#topSearchLine > div:nth-child(1) > form:nth-child(1) > div:nth-child(1)' \
                            ' > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)'
        self.__GET_ELEMENT_SEARCH = '#right > h3'
        self.__LANGUAGE_CHOICE = 'li.top-language:nth-child(4) > a:nth-child(1)'
        self.__GET_ELEMENT_LANGUAGE = 'li.top-language:nth-child(4) > a'
        self.__CATALOG_TYPE = '.slideBox>li>div>a'

        #EXPECTED
        self.EXPECTED_NAV_LINK_TEXT = 'Главная,О магазине,Гарантия,Доставка,Кредит,Онлайн кредит,Вопрос-ответ,Контакты,O!'
        self.EXPECTED_CATALOG_TEXT_PRODUCT = \
            'Мобильные телефоны,Устройства О!,Аксессуары,Сумки,Часы,SIM-карты O!,Гаджеты,Электросамокаты'
        self.EXPECTED_GET_SEARCH = 'Товары по запросу: «часы»'
        self.EXPECTED_GET_CATALOG = 'Новинки,Рассрочка 0-0-6,Флагман'

    @allure.step('locator элементов "Заголовка"')
    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__NAV_LINKS, 'Header Navigation Links')

    @allure.step('Принимать список виде "str"')
    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return Utils.join_strings(nav_links_text)

    @allure.step('Элементы по индексу'
                 'для взаимодействия')
    def get_nav_link_by_name(self, name) -> WebElement:
        elements = self.get_nav_links()
        return self.get_elemet_by_text(elements, name)

    @allure.step('locator элементов "Категории"')
    def get_catalog_product(self) -> List[WebElement]:
        return self.are_visible('css', self.__CATALOG_PRODUCT, 'Header Navigation Links')

    @allure.step('Принимать список виде "str"')
    def get_catalog_product_text(self) -> str:
        catalog_products = self.get_catalog_product()
        catalog_products_text = self.get_text_from_webelements(catalog_products)
        return Utils.join_strings(catalog_products_text)

    @allure.step('Элементы по индексу, для взаимодействия')
    def get_catalog_by_name(self, name) -> WebElement:
        elements = self.get_catalog_product()
        return self.get_elemet_by_text(elements, name)

    @allure.step('locator элемента "Поисковик"')
    def write_search(self):
        return self.is_visible('css', self.__SEARCH_WRITE, 'error element')

    @allure.step('Нажатие на кнопку')
    def click_search(self):
        return self.is_visible('css', self.__CLICK_SEARCH, 'error element')

    @allure.step('Написать в поле поисковика')
    def write_search_click_and_clear(self, text):
        element = self.write_search()
        return self.send_keys_custom(element, text)

    @allure.step('Элемент полученный от поисковика')
    def get_search_element(self):
        return self.is_visible('css', self.__GET_ELEMENT_SEARCH, 'error element')

    @allure.step('locator элемента "Языковые изменения"')
    def language_choice(self):
        return self.is_visible('css', self.__LANGUAGE_CHOICE, 'error element')

    @allure.step('locator элемента "Языковые изменения"')
    def get_language_element(self):
        return self.is_visible('css', self.__GET_ELEMENT_LANGUAGE, 'error element')

    @allure.step('locator элемента "Каталог"')
    def catalog_type(self) -> List[WebElement]:
        return self.are_visible('css', self.__CATALOG_TYPE, 'error element')

    @allure.step('Принимать список виде "str"')
    def catalog_type_get_text(self) -> str:
        catalog_type = self.catalog_type()
        catalog_type_texts = self.get_text_from_webelements(catalog_type)
        return Utils.join_strings(catalog_type_texts)
