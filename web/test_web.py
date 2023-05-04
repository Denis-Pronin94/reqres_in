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

from selenium import webdriver

from web.page import ListUsersPage


class TestWebReqresIn:
    """TestWebReqresIn."""

    def test_list_users(self, driver: webdriver):
        """Тест - test_list_users."""
        list_users = ListUsersPage(driver, 'https://reqres.in/')
        list_users.open()
        response, status = list_users.get_list_users()
        assert status == '200'
        try:
            ListUserSchema.parse_raw(response)
        except ValidationError as err:
            AssertionError(err)

    def test_single_users(self, driver: webdriver):
        """Тест - test_single_users."""
        single_users = ListUsersPage(driver, 'https://reqres.in/')
        single_users.open()
        response, status = single_users.get_single_users()
        assert status == '200'
        try:
            SingleUserSchema.parse_raw(response)
        except ValidationError as err:
            AssertionError(err)

    def test_single_users_not_found(self, driver: webdriver):
        """Тест - test_single_users_not_found."""
        single_users_not_found = ListUsersPage(driver, 'https://reqres.in/')
        single_users_not_found.open()
        response, status = single_users_not_found.get_single_users_not_found()
        assert response == '{}'
        assert status == '404'

    def test_list_resource(self, driver: webdriver):
        """Тест - test_list_resource."""
        list_resource = ListUsersPage(driver, 'https://reqres.in/')
        list_resource.open()
        response, status = list_resource.get_list_resource()
        assert status == '200'
        try:
            ListResourceSchema.parse_raw(response)
        except ValidationError as err:
            AssertionError(err)

    def test_single_resource(self, driver: webdriver):
        """Тест - test_single_resource."""
        single_resource = ListUsersPage(driver, 'https://reqres.in/')
        single_resource.open()
        response, status = single_resource.get_single_resource()
        assert status == '200'
        try:
            SingleResourceSchema.parse_raw(response)
        except ValidationError as err:
            AssertionError(err)

    def test_single_resource_not_fount(self, driver: webdriver):
        """Тест - test_single_resource_not_fount."""
        single_resource_not_fount = ListUsersPage(driver, 'https://reqres.in/')
        single_resource_not_fount.open()
        response, status = single_resource_not_fount.get_single_resource_not_fount()
        assert response == '{}'
        assert status == '404'

    def test_create_user(self, driver: webdriver):
        """Тест - test_create_user."""
        create_user = ListUsersPage(driver, 'https://reqres.in/')
        create_user.open()
        response, status = create_user.create_user()
        assert status == '201'
        try:
            CreateSchema.parse_raw(response)
        except ValidationError as err:
            AssertionError(err)

    def test_update_user_put(self, driver: webdriver):
        """Тест - test_update_user_put."""
        update_user_put = ListUsersPage(driver, 'https://reqres.in/')
        update_user_put.open()
        response, status = update_user_put.update_user_put()
        assert status == '200'
        try:
            UpdateSchema.parse_raw(response)
        except ValidationError as err:
            AssertionError(err)

    def test_update_user_patch(self, driver: webdriver):
        """Тест - test_update_user_patch."""
        update_user_patch = ListUsersPage(driver, 'https://reqres.in/')
        update_user_patch.open()
        response, status = update_user_patch.update_user_patch()
        assert status == '200'
        try:
            UpdateSchema.parse_raw(response)
        except ValidationError as err:
            AssertionError(err)

    def test_delete_user(self, driver: webdriver):
        """Тест - test_delete_user."""
        delete_user = ListUsersPage(driver, 'https://reqres.in/')
        delete_user.open()
        response, status = delete_user.delete_user()
        assert response == ''
        assert status == '204'

    def test_register_successful(self, driver: webdriver):
        """Тест - test_register_successful."""
        register_successful = ListUsersPage(driver, 'https://reqres.in/')
        register_successful.open()
        response, status = register_successful.register_successful()
        assert status == '200'
        try:
            RegisterSuccessfulSchema.parse_raw(response)
        except ValidationError as err:
            AssertionError(err)

    @pytest.mark.skip(
        reason='Баг - в ответе "error": "Note: Only defined users succeed registration".'
               'Должно быть "error": "Missing password".',
    )
    def test_register_unsuccessful(self, driver: webdriver):
        """Тест - test_register_unsuccessful."""
        register_unsuccessful = ListUsersPage(driver, 'https://reqres.in/')
        register_unsuccessful.open()
        response, status = register_unsuccessful.register_unsuccessful()
        assert response == {'error': 'Missing password'}
        assert status == '400'
        try:
            RegisterUnsuccessfulSchema.parse_raw(response)
        except ValidationError as err:
            AssertionError(err)

    def test_login_successful(self, driver: webdriver):
        """Тест - test_login_successful."""
        login_successful = ListUsersPage(driver, 'https://reqres.in/')
        login_successful.open()
        response, status = login_successful.login_successful()
        assert status == '200'
        try:
            LoginSuccessfulSchema.parse_raw(response)
        except ValidationError as err:
            AssertionError(err)

    @pytest.mark.skip(
        reason='Баг - в ответе "error": "user not found". '
               'Должно быть "error": "Missing password".',
    )
    def test_login_unsuccessful(self, driver: webdriver):
        """Тест - test_login_unsuccessful."""
        login_unsuccessful = ListUsersPage(driver, 'https://reqres.in/')
        login_unsuccessful.open()
        response, status = login_unsuccessful.login_unsuccessful()
        assert response == {'error': 'Missing password'}
        assert status == '400'
        try:
            LoginUnsuccessfulSchema.parse_raw(response)
        except ValidationError as err:
            AssertionError(err)

    def test_delayed_response(self, driver: webdriver):
        """Тест - test_delayed_response."""
        delayed_response = ListUsersPage(driver, 'https://reqres.in/')
        delayed_response.open()
        response, status = delayed_response.delayed_response()
        assert status == '200'
        try:
            ListUserSchema.parse_raw(response)
        except ValidationError as err:
            AssertionError(err)
