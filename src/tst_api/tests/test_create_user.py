from allure import step, title
from src.modules.helpers.randomizers.fake import Fake
from src.tst_api.service_model.reqres_in.model import CreateUser, AllUsers
from src.tst_api.service_model.reqres_in.rest import Reqres


class TestCreateUser:

    @title('Создание пользователя')
    def test_create_user(self):
        user_create = Reqres()

        with step('Отправляем запрос на создание пользователя'):
            name = Fake.random_full_name()
            job = Fake.random_job()
            response = user_create.post_create_user(name=name, job=job)
        with step('Проверяем соответствие типов данных'):
            CreateUser.model_validate(response.json())
        with step('Проверяем что передаваемые данные сохранились корректно'):
            assert response.json()['name'] == name
            assert response.json()['job'] == job

    def test_get_all_users(self):
        users = Reqres()

        with step('Отправляем запрос на получение данных пользователей'):
            response = users.get_users()
        with step('Проверяем соответствие типов данных'):
            AllUsers.parse_obj(response.json())
