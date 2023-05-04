from api.client import users_client

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def client() -> users_client:
    """Возвращаем клиент."""
    return users_client


@pytest.fixture()
def payload_user() -> dict:
    """Получаем тело запроса."""
    return {
        "name": "morpheus",
        "job": "leader",
    }


@pytest.fixture()
def payload_register() -> dict:
    """Получаем тело запроса."""
    return {
        "email": "eve.holt@reqres.in",
        "password": "pistol",
    }


@pytest.fixture()
def driver():
    """Фикстура driver."""
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    yield driver
    driver.quit()
