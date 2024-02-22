import time

from playwright.sync_api import Page

from src.tests.ui.modules.pages.login_page import LoginPage


def test(page: Page):
    login_page = LoginPage(page)
    login_page.log_in()
    time.sleep(5)

