import os

from playwright.sync_api import Page
from allure import step
from dotenv import load_dotenv

from src.tests.ui.modules.helpers.timeouts import Timeouts


class LoginPage:
    """Класс описывающий элементы на странице авторизации"""

    URL = 'index.php?action=Login&module=Users'

    def __init__(self, page: Page):
        self._page = page
        self.login_input = self._page.locator('#user_name')
        self.password_input = self._page.locator('#username_password')
        self.log_in_button = self._page.locator('#bigbutton')

    def open(self):
        with step(f'Открываем эндпоинт {self.URL}'):
            self._page.goto(self.URL)
            return self

    def log_in(self):
        """Функция для авторизации"""
        load_dotenv()
        self.open()
        with step('Авторизуемся на сайте'):
            self.login_input.fill(os.getenv('LOGIN'))
            self.password_input.fill(os.getenv('PASSWORD'))
            self.log_in_button.click(timeout=Timeouts.element_timeout)
