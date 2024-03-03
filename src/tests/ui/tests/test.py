from allure import step, title
from playwright.sync_api import Page, expect

from src.tests.ui.modules.base_objects.elemients.dropdown_all.individual import Individual
from src.tests.ui.modules.base_objects.elemients.header import Header
from src.tests.ui.modules.helpers.timeouts import Timeouts
from src.tests.ui.modules.pages.login_page import LoginPage


@title('ТК_А1 - Создание физического лица')
def test_create_fl(page: Page):
    login_page = LoginPage(page)
    header = Header(page)
    individual = Individual(page)
    create_fl_page = individual.CreateAnIndividual(page)

    login_page.log_in()
    header.open_link_individuals()
    with step(f'Переходим на страницу "Создать физическое лицо"'):
        individual.create_individual_button.click()
    create_fl_page.fill_full_name()
    with step('Выбираем категорию контакта'):
        create_fl_page.contact_category_select.select_option(label='Кандидат')
    with step('Переключение фокусировки браузера на новое открытое окно браузера'):
        search_company_page = Individual.CreateAnIndividual.CompanySearch(page)
        with step('Заполняем поле ИНН'):
            search_company_page.inn_input.fill('6321277661')
        with step('Выполняем клик по кнопке Найти'):
            search_company_page.search_button.click(timeout=Timeouts.element_timeout)
        with step('Выполняем клик по первой найденной компании'):
            search_company_page.company.click(timeout=Timeouts.element_timeout)
    create_fl_page.select_position(position='менеджер')
    create_fl_page.fill_phone_number()
    create_fl_page.fill_email()
    with step('Выполняем клик по кнопке "Сохранить и выйти"'):
        create_fl_page.save_and_exit_button.click(timeout=Timeouts.element_timeout)
    with step('Переключение фокусировки браузера на новую вкладку с данными о созданном ФЛ'):
        created_user_page = Individual.CreateAnIndividual.CreatedUser(page)
        with step('Проверяем ФИО, на соответствие введенному ФИО при регистрации'):
            expect(created_user_page.last_name_txt).to_have_text('АВТО')
            expect(created_user_page.first_name_txt).to_have_text('ТЕСТ')
            expect(created_user_page.middle_name_txt).to_have_text('ТЕСТОВИЧ')
        with step('Проверяем, что сохранились корректные данные в полях: "Категория контакта", "Предприятие"'):
            expect(created_user_page.contact_category_txt).to_have_text('Кандидат')
            expect(created_user_page.enterprise_txt).to_have_text('ООО "СЕНТЯБРИНКА"')
        with step('Проверяем, что сохранились корректные данные в полях: "Телефон", "Email"'):
            expect(created_user_page.phone_number_txt).to_have_text('+77777777777')
            expect(created_user_page.email_txt).to_have_text('test@mail.ru')

