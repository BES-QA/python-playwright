from allure import step
from playwright.sync_api import Page

from src.tests.ui.modules.helpers.timeouts import Timeouts


class Header:
    """
    Класс, описывающий элементы хедера
    """

    def __init__(self, page: Page):
        self._page = page
        self.dropdown_menu_all = self._page.locator('#grouptab_1')
        self.module_tab_individuals = self._page.locator('.topnav.all ').get_by_text('Физические лица')

    def open_link_individuals(self):
        with step('Из общего дропдауна открываем страницу "ФИЗИЧЕСКИЕ ЛИЦА"'):
            self.dropdown_menu_all.hover()
            self.module_tab_individuals.click(timeout=Timeouts.element_timeout)
