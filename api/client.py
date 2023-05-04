from config import URL

import requests


BASE_URL_WITH_NO_VERSION_API = URL


class BaseClient:
    """Базовый класс для API-клиентов."""

    def __init__(self, api_version: str = ''):
        """Дефолтные url."""
        self.base_url_with_version_api = f'{BASE_URL_WITH_NO_VERSION_API}{api_version}'


class UsersClient(BaseClient):
    """UsersClient."""

    def __init__(self, api_version: str = ''):
        """Переопределяем __init__."""
        super().__init__(api_version)
        self.GET_LIST_USER_URL = f'{self.base_url_with_version_api}/users'
        self.LIST_RESOURCE_URL = f'{self.base_url_with_version_api}/unknown'
        self.REGISTER_SUCCESSFUL = f'{self.base_url_with_version_api}/register'
        self.LOGIN_SUCCESSFUL = f'{self.base_url_with_version_api}/login'

    def get_list_user(self, method: str = 'GET', page_id: int = 1) -> requests.Response:
        """Возвращает клиент для получения информации о пользователях."""
        return requests.request(
            method=method,
            url=self.GET_LIST_USER_URL,
            params={'page': page_id},
        )

    def get_single_user(self, method: str = 'GET', user_id: int = 1) -> requests.Response:
        """Возвращает клиент для получения информации о пользователе."""
        return requests.request(method=method, url=f'{self.GET_LIST_USER_URL}/{user_id}')

    def get_list_resource(self, method: str = 'GET') -> requests.Response:
        """Возвращает клиент для получения информации о пользователях."""
        return requests.request(method=method, url=self.LIST_RESOURCE_URL)

    """Возвращает клиент для получения информации о пользователе."""

    def get_single_resource(self, method: str = 'GET', user_id: int = 1) -> requests.Response:
        """Возвращает клиент для получения информации о пользователе."""
        return requests.request(method=method, url=f'{self.LIST_RESOURCE_URL}/{user_id}')

    def create_user(self, payload: dict, method: str = 'POST') -> requests.Response:
        """Возвращает клиент для создания пользователя."""
        return requests.request(method=method, url=self.GET_LIST_USER_URL, json=payload)

    def update_user(
            self,
            payload: dict,
            method: str = 'PUT',
            user_id: int = 1,
    ) -> requests.Response:
        """Возвращает клиент для обновления данных пользователя."""
        return requests.request(
            method=method,
            url=f'{self.GET_LIST_USER_URL}/{user_id}',
            json=payload,
        )

    def delete_user(self, method: str = 'DELETE', user_id: int = 1) -> requests.Response:
        """Возвращает клиент для удаления пользователя."""
        return requests.request(
            method=method,
            url=f'{self.GET_LIST_USER_URL}/{user_id}',
        )

    def register_successful(self, payload: dict, method: str = 'POST') -> requests.Response:
        """Возвращает клиент для регистрации пользователя."""
        return requests.request(
            method=method,
            url=self.REGISTER_SUCCESSFUL,
            json=payload,
        )

    def login_successful(self, payload: dict, method: str = 'POST') -> requests.Response:
        """Возвращает клиент для регистрации логина."""
        return requests.request(
            method=method,
            url=self.LOGIN_SUCCESSFUL,
            json=payload,
        )

    def delayed_response(self, method: str = 'GET', delay: int = 1) -> requests.Response:
        """Возвращает клиент для получения информации о пользователях через определенное время."""
        return requests.request(
            method=method,
            url=self.GET_LIST_USER_URL,
            params={'delay': delay},
        )


users_client = UsersClient()
