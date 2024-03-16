import requests
from requests import Response


class Reqres:
    """
    Класс для взаимодействия с REST API сервиса <https://reqres.in>
    """

    def __init__(self):
        self._url = 'https://reqres.in'

    def post_create_user(self, name: str, job: str) -> Response:
        json = {
            'name': name,
            'job': job
        }
        return requests.post(url=self._url + '/tst_api/users', json=json)

    def get_users(self, page_num: str = '2'):
        return requests.get(url=self._url + f'/tst_api/users?page={page_num}')
