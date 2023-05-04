from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    """Базовый Page."""

    def __init__(self, driver: webdriver, url: str):
        """Базовый driver и url."""
        self.driver = driver
        self.url = url

    def open(self):
        """Открыть браузер."""
        self.driver.get(self.url)

    def element_is_visible(self, locator: str, timeout: int = 5) -> wait.mro():
        """Видимый элемент."""
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_present(self, locator: str, timeout: int = 8) -> wait.mro():
        """Не обязательно видимый элемент."""
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def go_to_element(self, element: str):
        """Переместиться к элементу."""
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
