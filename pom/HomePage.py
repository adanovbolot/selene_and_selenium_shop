from typing import List

import pytest

from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement


class HomePage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__NAV_LINKS = 'div.leftColumn > ul > li > a'
        self.NAV_LINK_TEXT = 'Главная,О магазине,Гарантия,Доставка,Кредит,Онлайн кредит,FAQ,Контакты,O!'

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__NAV_LINKS, 'Header Navigation Links')


    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return ','.join(nav_links_text)

