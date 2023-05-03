import requests

NO_VERSION_API = ''
VERSION_API_V1 = '/v1/'
VERSION_API_V2 = '/v2/'
BASE_URL_WITH_NO_VERSION_API = f'https://reqres.in/api{NO_VERSION_API}'
BASE_URL_WITH_VERSION_API_V1 = f'https://reqres.in/api{VERSION_API_V1}'
BASE_URL_WITH_VERSION_API_V2 = f'https://reqres.in/api{VERSION_API_V2}'


class BaseClient:
    """Базовый класс для API-клиентов."""

    def __init__(self):
        """Дефолтные url."""
        self.base_url_with_no_version_api = BASE_URL_WITH_NO_VERSION_API
        self.base_url_with_version_api_v1 = BASE_URL_WITH_VERSION_API_V1
        self.base_url_with_version_api_v2 = BASE_URL_WITH_VERSION_API_V2


class UsersClient(BaseClient):
    """UsersClient."""

    GET_LIST_USER_URL = f'{BASE_URL_WITH_NO_VERSION_API}/users'

    def get_list_user(self, method: str = 'GET', params: str = 1) -> requests.Response:
        """Возвращает клиент для получения информации о пользователях."""
        return requests.request(method=method, url=f'{self.GET_LIST_USER_URL}?page={params}')

    def get_single_user(self, method: str = 'GET', params: int = 1) -> requests.Response:
        """Возвращает клиент для получения информации о пользователе."""
        return requests.request(method=method, url=f'{self.GET_LIST_USER_URL}/{params}')

    LIST_RESOURCE_URL = f'{BASE_URL_WITH_NO_VERSION_API}/unknown'

    def get_list_resource(self, method: str = 'GET') -> requests.Response:
        """Возвращает клиент для получения информации о пользователях."""
        return requests.request(method=method, url=f'{self.LIST_RESOURCE_URL}')

    """Возвращает клиент для получения информации о пользователе."""

    def get_single_resource(self, method: str = 'GET', params: str = 1) -> requests.Response:
        """Возвращает клиент для получения информации о пользователе."""
        return requests.request(method=method, url=f'{self.GET_LIST_USER_URL}/{params}')

    def post_create(self, payload: dict, method: str = 'POST') -> requests.Response:
        """Возвращает клиент для создания пользователя."""
        return requests.request(method=method, url=f'{self.GET_LIST_USER_URL}', json=payload)

    def put_update(self, payload: dict, method: str = 'PUT', params: int = 1) -> requests.Response:
        """Возвращает клиент для обновления данных пользователя."""
        return requests.request(
            method=method,
            url=f'{self.GET_LIST_USER_URL}/{params}',
            json=payload,
        )

    def patch_update(
            self,
            payload: dict,
            method: str = 'PATCH',
            params: int = 1,
    ) -> requests.Response:
        """Возвращает клиент для обновления данных пользователя."""
        return requests.request(
            method=method,
            url=f'{self.GET_LIST_USER_URL}/{params}',
            json=payload,
        )

    def delete(self, method: str = 'DELETE', params: int = 1) -> requests.Response:
        """Возвращает клиент для удаления пользователя."""
        return requests.request(
            method=method,
            url=f'{self.GET_LIST_USER_URL}/{params}',
        )

    POST_REGISTER_SUCCESSFUL = f'{BASE_URL_WITH_NO_VERSION_API}/register'

    def register_successful(self, payload: dict, method: str = 'POST') -> requests.Response:
        """Возвращает клиент для удаления пользователя."""
        return requests.request(
            method=method,
            url=self.POST_REGISTER_SUCCESSFUL,
            json=payload,
        )


users_client = UsersClient()
