import random
from http import HTTPStatus

from data import (
    ids_not_valid_data_register,
    ids_not_valid_data_user,
    ids_valid_data_register,
    ids_valid_data_user,
    ids_wrong_user_id,
    not_valid_data_register,
    not_valid_data_user,
    valid_data_register,
    valid_data_user,
    wrong_user_id,
)

from jsonschema import ValidationError

import pytest

from schemas import (
    CreateSchema,
    ListResourceSchema,
    ListUserSchema,
    LoginSuccessfulSchema,
    LoginUnsuccessfulSchema,
    RegisterSuccessfulSchema,
    RegisterUnsuccessfulSchema,
    SingleResourceSchema,
    SingleUserSchema,
    UpdateSchema,
)


class TestListUsers:
    """Тест ендпоинта LIST USERS."""

    def test_get_list_user(self, client):
        """Позитивный тест - возвращает список пользователей на странице."""
        response = client.get_list_user(page_id=random.randint(1, 9999))
        assert response.status_code == HTTPStatus.OK
        try:
            ListUserSchema.parse_obj(response.json())
        except ValidationError as err:
            AssertionError(err)

    @pytest.mark.skip(
        reason='Баг - Статус код 200 при отправке запроса с невалидным параметром, '
               'должен быть 400.',
    )
    @pytest.mark.parametrize(
        'page_id',
        [
            0,
            'rick9999',
            '!!!',
            '.',
            ',',
            '.2',
            ',2',
            '2.',
            '2,',
            '@#$^&',
        ],
    )
    def test_wrong_page_id(self, client, page_id: int):
        """Негативный тест - передача невалидного параметра в url."""
        response = client.get_list_user(page_id=page_id)
        assert response.status_code == HTTPStatus.BAD_REQUEST


class TestSingleUsers:
    """Тест ендпоинта SINGLE USER."""

    def test_get_single_user(self, client):
        """Позитивный тест - возвращает одного пользователя."""
        response = client.get_single_user(user_id=random.randint(1, 12))
        assert response.status_code == HTTPStatus.OK
        try:
            SingleUserSchema.parse_obj(response.json())
        except ValidationError as err:
            AssertionError(err)

    @pytest.mark.parametrize(
        'user_id',
        wrong_user_id,
        ids=ids_wrong_user_id,
    )
    def test_wrong_user_id(self, client, user_id: int):
        """Негативный тест - передача невалидного параметра в url."""
        response = client.get_single_user(user_id=user_id)
        assert response.status_code == HTTPStatus.NOT_FOUND


class TestListResource:
    """Тест ендпоинта LIST <RESOURCE>."""

    def test_list_resource(self, client):
        """Позитивный тест - возвращает список пользователей."""
        response = client.get_list_resource()
        assert response.status_code == HTTPStatus.OK
        try:
            ListResourceSchema.parse_obj(response.json())
        except ValidationError as err:
            AssertionError(err)


class TestSingleResource:
    """Тест ендпоинта Single <RESOURCE>."""

    def test_single_resource(self, client):
        """Позитивный тест - возвращает одного пользователя."""
        response = client.get_single_resource(user_id=random.randint(1, 12))
        assert response.status_code == HTTPStatus.OK
        try:
            SingleResourceSchema.parse_obj(response.json())
        except ValidationError as err:
            AssertionError(err)

    @pytest.mark.parametrize(
        'user_id',
        wrong_user_id,
        ids=ids_wrong_user_id,
    )
    def test_wrong_user_id(self, client, user_id: int):
        """Негативный тест - передача невалидного параметра в url."""
        response = client.get_single_resource(user_id=user_id)
        assert response.status_code == HTTPStatus.NOT_FOUND


class TestCreate:
    """Тест ендпоинта Create."""

    @pytest.mark.parametrize(
        'payload',
        valid_data_user,
        ids=ids_valid_data_user,
    )
    def test_create_user(self, client, payload: dict):
        """Позитивный тест - создаёт одного пользователя."""
        response = client.create_user(payload=payload)
        assert response.status_code == HTTPStatus.CREATED
        try:
            CreateSchema.parse_obj(response.json())
        except ValidationError as err:
            AssertionError(err)

    @pytest.mark.skip(
        reason='Нет валидации тела запроса. Всегда возвращается статус 201.'
               'Должно 400.',
    )
    @pytest.mark.parametrize(
        'payload',
        not_valid_data_user,
        ids=ids_not_valid_data_user,
    )
    def test_create_with_wrong_payload(self, client, payload: dict):
        """Негативный тест - невалидный payload."""
        response = client.create_user(payload=payload)
        assert response.status_code == HTTPStatus.BAD_REQUEST


class TestUpdateUserPut:
    """Тест ендпоинта Update."""

    @pytest.mark.parametrize(
        'method',
        [
            'PATCH',
            'PUT',
        ],
    )
    @pytest.mark.parametrize(
        'payload',
        valid_data_user,
        ids=ids_valid_data_user,
    )
    def test_update(self, client, payload: dict, method: str):
        """Позитивный тест - обновляет данные пользователя."""
        response = client.update_user(payload=payload, method=method)
        assert response.status_code == HTTPStatus.OK
        try:
            UpdateSchema.parse_obj(response.json())
        except ValidationError as err:
            AssertionError(err)

    @pytest.mark.skip(
        reason='Нет валидации тела запроса. Всегда возвращается статус 200.'
               'Должно 400.',
    )
    @pytest.mark.parametrize(
        'method',
        [
            'PATCH',
            'PUT',
        ],
    )
    @pytest.mark.parametrize(
        'payload',
        not_valid_data_user,
        ids=ids_not_valid_data_user,
    )
    def test_update_with_wrong_payload(self, client, payload: dict, method: str):
        """Негативный тест - передача невалидного payload в теле запроса."""
        response = client.update_user(payload=payload, method=method)
        assert response.status_code == HTTPStatus.NOT_FOUND


class TestDelete:
    """Тест ендпоинта Delete."""

    def test_delete(self, client):
        """Позитивный тест - удаляет пользователя."""
        response = client.delete_user(user_id=random.randint(1, 9999))
        assert response.status_code == HTTPStatus.NO_CONTENT

    @pytest.mark.skip(
        reason='Нет валидации на передаваемый параметр. Всегда возвращается статус код 204.'
               'Должно 400.',
    )
    @pytest.mark.parametrize(
        'user_id',
        [
            -1,
            0,
            '-1',
            '0',
            'morpheus',
            True,
            '!.234,.#$%^&',
        ],
    )
    def test_wrong_id_user(self, client, user_id: int):
        """Негативный тест - передача невалидного параметра в url."""
        response = client.delete_user(user_id=user_id)
        assert response.status_code == HTTPStatus.BAD_REQUEST


class TestRegisterSuccessful:
    """Тест ендпоинта REGISTER - SUCCESSFUL."""

    @pytest.mark.parametrize(
        'payload',
        valid_data_register,
        ids=ids_valid_data_register,
    )
    def test_register_successful(self, client, payload: dict):
        """Позитивный тест - проверяет успешную регистрацию."""
        response = client.register_successful(payload=payload)
        assert response.status_code == HTTPStatus.OK
        try:
            RegisterSuccessfulSchema.parse_obj(response.json())
        except ValidationError as err:
            AssertionError(err)

    @pytest.mark.skip(
        reason='Баг - в ответе "error": "Note: Only defined users succeed registration".'
               'Должно быть "error": "Missing password".',
    )
    @pytest.mark.parametrize(
        'payload',
        not_valid_data_register,
        ids=ids_not_valid_data_register,
    )
    def test_register_with_wrong_payload(self, client, payload: dict):
        """Негативный тест - передача невалидного payload в теле запроса."""
        response = client.register_successful(payload=payload)
        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json() == {'error': 'Missing password'}
        try:
            RegisterUnsuccessfulSchema.parse_obj(response.json())
        except ValidationError as err:
            AssertionError(err)


class TestLoginSuccessful:
    """Тест ендпоинта LOGIN - SUCCESSFUL."""

    @pytest.mark.parametrize(
        'payload',
        valid_data_register,
        ids=ids_valid_data_register,
    )
    def test_login_successful(self, client, payload: dict):
        """Позитивный тест - проверяет успешную регистрацию."""
        response = client.login_successful(payload=payload)
        assert response.status_code == HTTPStatus.OK
        try:
            LoginSuccessfulSchema.parse_obj(response.json())
        except ValidationError as err:
            AssertionError(err)

    @pytest.mark.skip(
        reason='Баг - в ответе "error": "user not found". '
               'Должно быть "error": "Missing password".',
    )
    @pytest.mark.parametrize(
        'payload',
        not_valid_data_register,
        ids=ids_not_valid_data_register,
    )
    def test_login_successful_with_wrong_payload(self, client, payload: dict):
        """Негативный тест - передача невалидного payload в теле запроса."""
        response = client.login_successful(payload=payload)
        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json() == {'error': 'Missing password'}
        try:
            LoginUnsuccessfulSchema.parse_obj(response.json())
        except ValidationError as err:
            AssertionError(err)


class TestDelayedResponse:
    """Тест ендпоинта Delayed Response."""

    def test_get_list_user_delayed_response(self, client):
        """Позитивный тест - возвращает список пользователей на странице через рандомное время."""
        random_second = random.randint(0, 10)
        response = client.delayed_response(delay=random_second)
        assert response.status_code == HTTPStatus.OK
        assert int(response.elapsed.total_seconds()) == random_second
        try:
            ListUserSchema.parse_obj(response.json())
        except ValidationError as err:
            AssertionError(err)

    @pytest.mark.skip(
        reason='Баг - Статус код 200 при отправке запроса с невалидным параметром.'
               'Должно 400.',
    )
    @pytest.mark.parametrize(
        'delay',
        [
            -5,
            '.',
            ',',
            '.2',
            ',2',
            '2.',
            '2,',
            '@#$^&.,',
            'morpheus',
        ],
    )
    def test_wrong_delay(self, client, delay: int):
        """Негативный тест - передача невалидного параметра в url."""
        response = client.delayed_response(delay=delay)
        assert response.status_code == HTTPStatus.BAD_REQUEST


class TestWrongMethod:
    """TestWrongMethod."""

    @pytest.mark.skip(
        reason='При отправке запроса с неправильным методом не возвращается статус код 405.'
               'Возвращается 201, 204, 404',
    )
    @pytest.mark.parametrize(
        'client_method, wrong_methods_list',
        [
            ('get_list_user', ['POST', 'PUT', 'DELETE', 'PATCH']),
            ('get_single_user', ['POST', 'PUT', 'DELETE', 'PATCH']),
            ('get_list_resource', ['POST', 'PUT', 'DELETE', 'PATCH']),
            ('get_single_resource', ['POST', 'PUT', 'DELETE', 'PATCH']),
            ('create_user', ['GET', 'PUT', 'DELETE', 'PATCH']),
            ('update_user', ['POST', 'DELETE']),
            ('delete_user', ['POST', 'PUT', 'GET', 'PATCH']),
            ('register_successful', ['GET', 'PUT', 'DELETE', 'PATCH']),
            ('login_successful', ['GET', 'PUT', 'DELETE', 'PATCH']),
            ('delayed_response', ['POST', 'PUT', 'DELETE', 'PATCH']),
        ],
    )
    def test_wrong_methods_not_allowed(self, client, client_method: str, wrong_methods_list: list):
        """Негативный тест - отправка запроса с неправильным методом."""
        for method in wrong_methods_list:
            client_with_method = getattr(client, client_method)
            response = client_with_method(method=method)
            assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
