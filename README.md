# Проект по автоматизации тестирования на сайте - reqres.in.
> <a target="_blank" href="https://reqres.in/">Ссылка на страницу сайта</a>

В этом репозитории я тестировал REST-API, а так же писал UI автотесты
https://reqres.in/ на языке python 3.10.

Использовал:
- IDE PyCharm для написания кода;
- виртуальное окружение Poetry для управления зависимостями в Python проектах;
- Pytest для написания и выполнения тестового кода;
- Библеотеку Requests, позволяющую отправлять HTTP запросы;
- Pydantic для валидации и анализа данных;
- Selenium WebDriver для управления браузерам;
- библеотеку webdriver-manager для автоматического скачивания вебдрайвера;

Особенности проекта:
- Тесты параметризированны. Применил декоратор @pytest.mark.parametrize, куда передавал параметры;
- В файле client.py созданы клиенты. На каждый endpoint создан свой клиент;
- Валидировал response json с помощью созданной схемы (Pydantic).
