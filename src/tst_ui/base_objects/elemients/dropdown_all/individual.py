from allure import step
from playwright.sync_api import Page

from src.modules.helpers.timeouts import Timeouts


class Individual:
    """Класс, описывающий страницу 'ФИЗИЧЕСКИЕ ЛИЦА'"""

    def __init__(self, page: Page):
        self.page = page
        self.create_individual_button = page.get_by_role("link", name='Создать физическое лицо')

    class CreateAnIndividual:
        """Класс, описывающий страницу 'СОЗДАТЬ'"""

        def __init__(self, page: Page):
            self._page = page
            self.last_name_input = self._page.locator('#last_name')
            self.first_name_input = self._page.locator('#first_name')
            self.middle_name_input = self._page.locator('#second_name')
            self.contact_category_select = self._page.locator('#contact_category')
            self.position_select = self._page.locator('#position')
            self.phone_number_input = self._page.locator('input[name="phone_numberContacts0"]')
            self.email_input = self._page.get_by_role("textbox", name="адрес E-mail")
            self.save_and_exit_button = self._page.locator('#SAVE').last
            self.select_account_button = self._page.get_by_title('Select Account')

        def fill_full_name(self,
                           last_name: str = 'Авто',
                           first_name: str = 'Тест',
                           middle_name: str = 'Тестович'):
            """Функция для заполнения ФИО"""
            with step('Заполняем поля ФИО'):
                self.last_name_input.fill(last_name)
                self.first_name_input.fill(first_name)
                self.middle_name_input.fill(middle_name)

        def select_position(self, position: str):
            """Функция для выбора должности.
            Должность необходимо указывать в точности как на странице"""
            with step('Выбираем должность кандидата'):
                self.position_select.fill(position)
                self.position_select.press('Backspace', delay=500)
                self.position_select.press('Enter', delay=500)
                self._page.get_by_text(position, exact=True).click(timeout=Timeouts.element_timeout)

        def fill_phone_number(self, number: str = '7777777777'):
            """Функция для заполнения номера телефона"""
            with step('Заполняем номер телефона'):
                self.phone_number_input.click(timeout=Timeouts.element_timeout)
                self.phone_number_input.fill(number)
                self.phone_number_input.press('Enter', delay=1000)

        def fill_email(self, email: str = 'test@mail.ru'):
            """Функция для заполнения email"""
            with step('Заполняем поле E-mail'):
                self.email_input.fill(email)
                self.email_input.press('Enter', delay=1000)

        class CompanySearch:
            """Класс, описывающий страницу 'Поиск предприятий'"""

            def __init__(self, page: Page):
                self._page = page
                self._new_tab = self.switch_to_company_search_page()
                self.inn_input = self._new_tab.get_by_label('ИНН')
                self.search_button = self._new_tab.get_by_role('button', name='Найти')
                self.company = self._new_tab.locator('tbody').locator('[valign="top"] a').nth(0)

            def switch_to_company_search_page(self):
                """Функция для переключения на окно браузера с новой страницей 'Поиск предприятия'"""
                with self._page.expect_popup() as _new_tab:
                    Individual.CreateAnIndividual(page=self._page) \
                        .select_account_button \
                        .click(timeout=Timeouts.element_timeout)
                return _new_tab.value

        class SaveFL:
            """Класс, описывающий страницу 'СОХРАНИТЬ ФИЗ. ЛИЦО'"""

            def __init__(self, page: Page):
                self._page = page
                self.first_name_txt = self._page.locator('.oddListRowS1 a').first
                self.last_name_txt = self._page.locator('.oddListRowS1 a').nth(1)
                self.middle_name_txt = self._page.locator('.oddListRowS1 a').nth(2)
                self.first_created_user_link = self._page.locator('.oddListRowS1 a').first

        class CreatedUser:
            """Класс, описывающий страницу с данными созданного пользователя"""

            def __init__(self, page: Page):
                self._page = page
                self._new_tab = self.switch_to_created_user_page()
                self.last_name_txt = self._new_tab.locator('#last_name')
                self.first_name_txt = self._new_tab.locator('#first_name')
                self.middle_name_txt = self._new_tab.locator('#second_name')
                self.contact_category_txt = self._new_tab.locator('[field="contact_category"]')
                self.enterprise_txt = self._new_tab.locator('#account_id')
                self.phone_number_txt = self._new_tab.locator('.multiphone-detail td')
                self.email_txt = self._new_tab.locator('.email-link')

            def switch_to_created_user_page(self):
                """Функция для переключения на вкладку созданного физического лица"""
                with self._page.expect_popup() as _new_tab:
                    Individual.CreateAnIndividual.SaveFL(self._page) \
                        .first_created_user_link \
                        .click(timeout=Timeouts.element_timeout)
                return _new_tab.value
