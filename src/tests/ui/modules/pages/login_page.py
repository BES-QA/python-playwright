import os

from playwright.sync_api import Page
from allure import step
from dotenv import load_dotenv


class LoginPage:
    URL = 'index.php?action=Login&module=Users'

    def __init__(self,
                 page: Page):
        self.page = page
        self.login_input = page.locator('#user_name')
        self.password_input = page.locator('#username_password')
        self.log_in_button = page.locator('#bigbutton')

    def open(self):
        with step(f'Открываем эндпоинт {self.URL}'):
            self.page.goto(self.URL)
            return self

    def log_in(self):
        """Функция для авторизации"""
        load_dotenv()
        self.open()
        with step('Авторизуемся на сайте'):
            self.login_input.fill(os.getenv('LOGIN'))
            self.password_input.fill(os.getenv('PASSWORD'))
            self.log_in_button.click()
