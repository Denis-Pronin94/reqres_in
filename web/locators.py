from selenium.webdriver.common.by import By


class ListLocators:
    """Локаторы."""

    LIST_USERS = (By.XPATH, '//li[@data-id="users"]')
    SINGLE_USER = (By.XPATH, '//li[@data-id="users-single"]')
    SINGLE_USER_NOT_FOUND = (By.XPATH, '//li[@data-id="users-single-not-found"]')
    LIST_RESOURCE = (By.XPATH, '//li[@data-id="unknown"]')
    SINGLE_RESOURCE = (By.XPATH, '//li[@data-id="unknown-single"]')
    SINGLE_RESOURCE_NOT_FOUND = (By.XPATH, '//li[@data-id="unknown-single-not-found"]')
    CREATE = (By.XPATH, '//li[@data-id="post"]')
    UPDATE_PUT = (By.XPATH, '//li[@data-id="put"]')
    UPDATE_PATCH = (By.XPATH, '//li[@data-id="patch"]')
    DELETE = (By.XPATH, '//li[@data-id="delete"]')
    REGISTER_SUCCESSFUL = (By.XPATH, '//li[@data-id="register-successful"]')
    REGISTER_UNSUCCESSFUL = (By.XPATH, '//li[@data-id="register-unsuccessful"]')
    LOGIN_SUCCESSFUL = (By.XPATH, '//li[@data-id="login-successful"]')
    LOGIN_UNSUCCESSFUL = (By.XPATH, '//li[@data-id="login-unsuccessful"]')
    DELAYED_RESPONSE = (By.XPATH, '//li[@data-id="delay"]')

    RESPONSE_LIST_USERS = (By.XPATH, '//pre[@data-key="output-response"]')
    STATUS = (By.XPATH, '//span[@data-key="response-code"]')
