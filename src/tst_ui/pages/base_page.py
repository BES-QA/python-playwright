from allure import step
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self._page = page

    def navigate(self, url: str = ''):
        with step(f'Переходим по адресу {url}'):
            self._page.goto(url)
            return self
