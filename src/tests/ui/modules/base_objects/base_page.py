from allure import step
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str = ''):
        with step(f'Переходим по адресу {url}'):
            self.page.goto(url)
            return self
