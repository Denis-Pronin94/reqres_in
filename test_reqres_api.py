import random
from http import HTTPStatus

from client import users_client

from data import (
    ids_not_valid_data_register,
    ids_not_valid_data_user,
    ids_valid_data_register,
    ids_valid_data_user,
    not_valid_data_register,
    not_valid_data_user,
    valid_data_register,
    valid_data_user,
)

from jsonschema import ValidationError

import pytest

from schemas import (
    CreateSchema,
    ListResourceSchema,
    ListUserSchema,
    RegisterSchema,
    SingleUserSchema,
    UpdateSchema,
)


class TestListUsers:
    """LIST USERS."""

    def test_get_list_user(self):
        """Позитивный тест - возвращает список пользователей на странице."""
        response = users_client.get_list_user(params=random.randint(1, 9999))
        assert response.status_code == HTTPStatus.OK
        try:
            ListUserSchema.parse_obj(response.json())
        except ValidationError as err:
            AssertionError(err)

    @pytest.mark.skip(
        reason='Баг - Статус код 200 при отправке запроса с невалидным параметром, '
               'должен быть 404.',
    )
    @pytest.mark.parametrize(
        'param',
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
    def test_wrong_param(self, param: str):
        """Негативный тест - передача невалидного параметра в url."""
        response = users_client.get_list_user(params=param)
        assert response.status_code == HTTPStatus.NOT_FOUND

    @pytest.mark.skip(
        reason='Баг - Статус код 201 при отправке запроса с методом POST, а должен быть 404.'
               'Статус код 204 при отправке запроса с методом DELETE, а должен быть 404.',
    )
    @pytest.mark.parametrize(
        'method',
        [
            'POST',
            'PUT',
            'DELETE',
            'PATCH',
        ],
    )
    def test_wrong_method(self, method: str):
        """Негативный тест - отправка запроса с неправильным методом."""
        response = users_client.get_list_user(method=method)
        assert response.status_code == HTTPStatus.NOT_FOUND


class TestSingleUsers:
    """SINGLE USER."""

    def test_get_single_user(self):
        """Позитивный тест - возвращает одного пользователей."""
        response = users_client.get_single_user(params=random.randint(1, 12))
        assert response.status_code == HTTPStatus.OK
        try:
            SingleUserSchema.parse_obj(response.json())
        except ValidationError as err:
            AssertionError(err)

    @pytest.mark.parametrize(
        'param',
        [
            0,
            'rick9999',
            '!!!',
            ',',
            '.2',
            ',2',
            '2,',
            '@#$^&',
            random.randint(13, 999),
        ],
    )
    def test_wrong_param(self, param: str):
        """Негативный тест - передача невалидного параметра в url."""
        response = users_client.get_single_user(params=param)
        assert response.status_code == HTTPStatus.NOT_FOUND

    @pytest.mark.skip(
        reason='Баг - Нет статуса Not Found при отправке запроса с неправильным методом.',
    )
    @pytest.mark.parametrize(
        'method',
        [
            'POST',
            'PUT',
            'DELETE',
            'PATCH',
        ],
    )
    def test_wrong_method(self, method: str):
        """Негативный тест - отправка запроса с неправильным методом."""
        response = users_client.get_single_users(method=method)
        assert response.status_code == HTTPStatus.NOT_FOUND


class TestListResource:
    """LIST <RESOURCE>."""

    def test_list_resource(self):
        """Позитивный тест - возвращает список пользователей."""
        response = users_client.get_list_resource()
        assert response.status_code == HTTPStatus.OK
        try:
            ListResourceSchema.parse_obj(response.json())
        except ValidationError as err:
            AssertionError(err)

    @pytest.mark.skip(
        reason='Баг - Нет статуса "Not Found" при отправке запроса с неправильным методом.',
    )
    @pytest.mark.parametrize(
        'method',
        [
            'POST',
            'PUT',
            'DELETE',
            'PATCH',
        ],
    )
    def test_wrong_method(self, method: str):
        """Негативный тест - отправка запроса с неправильным методом."""
        response = users_client.get_list_resource(method=method)
        assert response.status_code == HTTPStatus.NOT_FOUND


class TestSingleResource:
    """Single <RESOURCE>."""

    def test_single_resource(self):
        """Позитивный тест - возвращает одного пользователей."""
        response = users_client.get_single_resource(params=random.randint(1, 12))
        assert response.status_code == HTTPStatus.OK
        try:
            SingleUserSchema.parse_obj(response.json())
        except ValidationError as err:
            AssertionError(err)

    @pytest.mark.parametrize(
        'param',
        [
            0,
            'rick9999',
            '!!!',
            ',',
            '.2',
            ',2',
            '2,',
            '@#$^&',
            random.randint(13, 14),
        ],
    )
    def test_wrong_param(self, param: str):
        """Негативный тест - неправильный параметр."""
        response = users_client.get_single_resource(params=param)
        assert response.status_code == HTTPStatus.NOT_FOUND

    @pytest.mark.skip(
        reason='Баг - Неправильный статус ответа при отправке запроса с неправильным методом, '
               ' быть "Not Faund".',
    )
    @pytest.mark.parametrize(
        'method',
        [
            'POST',
            'PUT',
            'DELETE',
            'PATCH',
        ],
    )
    def test_wrong_method(self, method: str):
        """Негативный тест - отправка запроса с неправильным методом."""
        response = users_client.get_single_resource(method=method)
        assert response.status_code == HTTPStatus.NOT_FOUND


class TestCreate:
    """TestCreate."""

    @pytest.mark.parametrize(
        'payload',
        valid_data_user,
        ids=ids_valid_data_user,
    )
    def test_create(self, payload: dict):
        """Позитивный тест - создаёт одного пользователя."""
        response = users_client.post_create(payload=payload)
        assert response.status_code == HTTPStatus.CREATED
        try:
            CreateSchema.parse_obj(response.json())
        except ValidationError as err:
            AssertionError(err)

    @pytest.mark.skip(reason='Не валидации тела запроса. Всегда возвращается статус 201.')
    @pytest.mark.parametrize(
        'payload',
        not_valid_data_user,
        ids=ids_not_valid_data_user,
    )
    def test_wrong_payload(self, payload: dict):
        """Негативный тест - невалидный payload."""
        response = users_client.post_create(payload=payload)
        assert response.status_code == HTTPStatus.NOT_FOUND

    @pytest.fixture
    def payload_fixture(self) -> dict:
        """Получаем тело запроса."""
        return {
            "name": "morpheus",
            "job": "leader",
        }

    @pytest.mark.skip(
        reason='Баг - Статус код 201 при отправке запроса с методом POST, а должен быть 404.'
               'Статус код 204 при отправке запроса с методом DELETE, а должен быть 404.',
    )
    @pytest.mark.parametrize(
        'method',
        [
            'GET',
            'PUT',
            'DELETE',
            'PATCH',
        ],
    )
    def test_wrong_method(self, payload_fixture: dict, method: str):
        """Негативный тест - отправка запроса с неправильным методом."""
        response = users_client.post_create(payload=payload_fixture, method=method)
        assert response.status_code == HTTPStatus.NOT_FOUND


class TestUpdatePut:
    """TestUpdatePut."""

    @pytest.mark.parametrize(
        'payload',
        valid_data_user,
        ids=ids_valid_data_user,
    )
    def test_update(self, payload: dict):
        """Позитивный тест - обновляет данные пользователя."""
        response = users_client.put_update(payload=payload)
        assert response.status_code == HTTPStatus.OK
        try:
            UpdateSchema.parse_obj(response.json())
        except ValidationError as err:
            AssertionError(err)

    @pytest.mark.skip(reason='Нет валидации тела запроса. Всегда возвращается статус 200.')
    @pytest.mark.parametrize(
        'payload',
        not_valid_data_user,
        ids=ids_not_valid_data_user,
    )
    def test_wrong_payload(self, payload: dict):
        """Негативный тест - невалидный payload."""
        response = users_client.put_update(payload=payload)
        assert response.status_code == HTTPStatus.NOT_FOUND

    @pytest.fixture
    def payload_fixture(self) -> dict:
        """Получаем тело запроса."""
        return {
            "name": "morpheus",
            "job": "leader",
        }

    @pytest.mark.skip(
        reason='Нет валидации тела на метод запроса. '
               'При отправке запроса с любым методом всегда возвращается статус 200.',
    )
    @pytest.mark.parametrize(
        'method',
        [
            'GET',
            'POST',
            'DELETE',
            'PATCH',
        ],
    )
    def test_wrong_method(self, payload_fixture: dict, method: str):
        """Негативный тест - отправка запроса с неправильным методом."""
        response = users_client.put_update(payload=payload_fixture, method=method)
        assert response.status_code == HTTPStatus.NOT_FOUND


class TestUpdatePatch:
    """TestUpdatePatch."""

    @pytest.mark.parametrize(
        'payload',
        valid_data_user,
        ids=ids_valid_data_user,
    )
    def test_update(self, payload: dict):
        """Позитивный тест - обновляет данные пользователя."""
        response = users_client.patch_update(payload=payload)
        assert response.status_code == HTTPStatus.OK
        try:
            UpdateSchema.parse_obj(response.json())
        except ValidationError as err:
            AssertionError(err)

    @pytest.mark.skip(reason='Нет валидации тела запроса. Всегда возвращается статус 200.')
    @pytest.mark.parametrize(
        'payload',
        not_valid_data_user,
        ids=ids_not_valid_data_user,
    )
    def test_wrong_payload(self, payload: dict):
        """Негативный тест - невалидный payload."""
        response = users_client.patch_update(payload=payload)
        assert response.status_code == HTTPStatus.NOT_FOUND

    @pytest.fixture
    def payload_fixture(self) -> dict:
        """Получаем тело запроса."""
        return {
            "name": "morpheus",
            "job": "leader",
        }

    @pytest.mark.skip(
        reason='Нет валидации тела на метод запроса. '
               'При отправке запроса с любым методом всегда возвращается статус 200.',
    )
    @pytest.mark.parametrize(
        'method',
        [
            'GET',
            'POST',
            'DELETE',
            'PATCH',
        ],
    )
    def test_wrong_method(self, payload_fixture: dict, method: str):
        """Негативный тест - отправка запроса с неправильным методом."""
        response = users_client.patch_update(payload=payload_fixture, method=method)
        assert response.status_code == HTTPStatus.NOT_FOUND


class TestDelete:
    """TestDelete."""

    def test_delete(self):
        """Позитивный тест - удаляет пользователя."""
        response = users_client.delete(params=random.randint(1, 9999))
        assert response.status_code == HTTPStatus.NO_CONTENT

    @pytest.mark.skip(
        reason='Нет валидации на передаваемый параметр. Всегда возвращается статус код 204.',
    )
    @pytest.mark.parametrize(
        'id_user',
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
    def test_wrong_params(self, id_user: str):
        """Негативный тест - передача невалидного параметра в url."""
        response = users_client.delete(params=id_user)
        assert response.status_code == HTTPStatus.NOT_FOUND

    @pytest.mark.skip(
        reason='Нет валидации тела на метод запроса. '
               'При отправке запроса с любым методом всегда возвращается статус 200 или 201.',
    )
    @pytest.mark.parametrize(
        'method',
        [
            'GET',
            'POST',
            'PUT',
            'PATCH',
        ],
    )
    def test_wrong_method(self, method: str):
        """Негативный тест - отправка запроса с неправильным методом."""
        response = users_client.delete(method=method)
        assert response.status_code == HTTPStatus.NOT_FOUND


class TestRegisterSuccessful:
    """TestRegisterSuccessful."""

    @pytest.mark.parametrize(
        'payload',
        valid_data_register,
        ids=ids_valid_data_register,
    )
    def test_register_successful(self, payload: dict):
        """Позитивный тест - проверяет успешную регистрацию."""
        response = users_client.register_successful(payload=payload)
        assert response.status_code == HTTPStatus.OK
        try:
            RegisterSchema.parse_obj(response.json())
        except ValidationError as err:
            AssertionError(err)

    @pytest.mark.parametrize(
        'payload',
        not_valid_data_register,
        ids=ids_not_valid_data_register,
    )
    def test_wrong_payload(self, payload: dict):
        """Негативный тест - невалидный payload."""
        response = users_client.register_successful(payload=payload)
        assert response.status_code == HTTPStatus.BAD_REQUEST

    @pytest.fixture
    def payload_fixture(self) -> dict:
        """Получаем тело запроса."""
        return {
            "email": "eve.holt@reqres.in",
            "password": "pistol",
        }

    @pytest.mark.skip(
        reason='Баг - Статус код 200 при отправке запроса с методом GET, а должен быть 404.'
               'Статус код 204 при отправке запроса с методом DELETE, а должен быть 404.',
    )
    @pytest.mark.parametrize(
        'method',
        [
            'GET',
            'PUT',
            'DELETE',
            'PATCH',
        ],
    )
    def test_wrong_method(self, method: str, payload_fixture: dict):
        """Негативный тест - отправка запроса с неправильным методом."""
        response = users_client.register_successful(method=method, payload=payload_fixture)
        assert response.status_code == HTTPStatus.NOT_FOUND
