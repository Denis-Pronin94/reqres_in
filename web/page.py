from web.base_page import BasePage
from web.locators import ListLocators


class ListUsersPage(BasePage):
    """ListUsersPage."""

    locators = ListLocators()

    def get_list_users(self) -> tuple:
        """Возвращает список пользователей на странице."""
        self.element_is_visible(self.locators.LIST_USERS).click()
        response = self.element_is_visible(self.locators.RESPONSE_LIST_USERS).text
        status = self.element_is_visible(self.locators.STATUS).text
        return response, status

    def get_single_users(self) -> tuple:
        """Возвращает одного пользователя."""
        self.element_is_visible(self.locators.SINGLE_USER).click()
        response = self.element_is_visible(self.locators.RESPONSE_LIST_USERS).text
        status = self.element_is_visible(self.locators.STATUS).text
        return response, status

    def get_single_users_not_found(self) -> tuple:
        """Возвращает пустой список при невалидном параметре."""
        self.element_is_visible(self.locators.SINGLE_USER_NOT_FOUND).click()
        response = self.element_is_visible(self.locators.RESPONSE_LIST_USERS).text
        status = self.element_is_visible(self.locators.STATUS).text
        return response, status

    def get_list_resource(self) -> tuple:
        """Возвращает список пользователей на странице."""
        self.element_is_visible(self.locators.LIST_RESOURCE).click()
        response = self.element_is_visible(self.locators.RESPONSE_LIST_USERS).text
        status = self.element_is_visible(self.locators.STATUS).text
        return response, status

    def get_single_resource(self) -> tuple:
        """Возвращает одного пользователя."""
        self.element_is_visible(self.locators.SINGLE_RESOURCE).click()
        response = self.element_is_visible(self.locators.RESPONSE_LIST_USERS).text
        status = self.element_is_visible(self.locators.STATUS).text
        return response, status

    def get_single_resource_not_fount(self) -> tuple:
        """Возвращает пустой список при невалидном параметре."""
        self.element_is_visible(self.locators.SINGLE_RESOURCE_NOT_FOUND).click()
        response = self.element_is_visible(self.locators.RESPONSE_LIST_USERS).text
        status = self.element_is_visible(self.locators.STATUS).text
        return response, status

    def create_user(self) -> tuple:
        """Создаёт нового пользователя."""
        self.element_is_visible(self.locators.CREATE).click()
        response = self.element_is_visible(self.locators.RESPONSE_LIST_USERS).text
        status = self.element_is_visible(self.locators.STATUS).text
        return response, status

    def update_user_put(self) -> tuple:
        """Обновляет информация о пользователе."""
        self.element_is_visible(self.locators.UPDATE_PUT).click()
        response = self.element_is_visible(self.locators.RESPONSE_LIST_USERS).text
        status = self.element_is_visible(self.locators.STATUS).text
        return response, status

    def update_user_patch(self) -> tuple:
        """Обновляет информация о пользователе."""
        self.element_is_visible(self.locators.UPDATE_PATCH).click()
        response = self.element_is_visible(self.locators.RESPONSE_LIST_USERS).text
        status = self.element_is_visible(self.locators.STATUS).text
        return response, status

    def delete_user(self) -> tuple:
        """Удаляет пользователя."""
        self.element_is_visible(self.locators.DELETE).click()
        response = self.element_is_visible(self.locators.RESPONSE_LIST_USERS).text
        status = self.element_is_visible(self.locators.STATUS).text
        return response, status

    def register_successful(self) -> tuple:
        """Успешая регистрация."""
        self.element_is_visible(self.locators.REGISTER_SUCCESSFUL).click()
        response = self.element_is_visible(self.locators.RESPONSE_LIST_USERS).text
        status = self.element_is_visible(self.locators.STATUS).text
        return response, status

    def register_unsuccessful(self) -> tuple:
        """Не успешая регистрация."""
        self.element_is_visible(self.locators.REGISTER_UNSUCCESSFUL).click()
        response = self.element_is_visible(self.locators.RESPONSE_LIST_USERS).text
        status = self.element_is_visible(self.locators.STATUS).text
        return response, status

    def login_successful(self) -> tuple:
        """Успешное создание логина."""
        self.element_is_visible(self.locators.LOGIN_SUCCESSFUL).click()
        response = self.element_is_visible(self.locators.RESPONSE_LIST_USERS).text
        status = self.element_is_visible(self.locators.STATUS).text
        return response, status

    def login_unsuccessful(self) -> tuple:
        """Не успешное создание логина."""
        self.element_is_visible(self.locators.LOGIN_UNSUCCESSFUL).click()
        response = self.element_is_visible(self.locators.RESPONSE_LIST_USERS).text
        status = self.element_is_visible(self.locators.STATUS).text
        return response, status

    def delayed_response(self) -> tuple:
        """Возвращает список пользователей на странице через некоторое время."""
        self.element_is_visible(self.locators.DELAYED_RESPONSE).click()
        response = self.element_is_visible(self.locators.RESPONSE_LIST_USERS).text
        status = self.element_is_visible(self.locators.STATUS).text
        return response, status
