# Автоматизированные тесты для [Stellar Burgers](https://stellarburgers.nomoreparties.site/)

Stellar Burgers - это онлайн-платформа для заказа вымышленных космических бургеров.

## Обзор

Этот репозиторий содержит автоматизированные тесты для веб-приложения Stellar Burgers, реализованные с использованием Selenium WebDriver и Python.

## Используемые технологии

- Python 3.11.9
- Selenium WebDriver 4.21.0
- Pytest
- Faker (для генерации случайных тестовых данных)

## Описания тестов

### test_registration_page.py

- **test_successful_registration**: Тестирует успешную регистрацию нового пользователя.
- **test_unsuccessful_registration_with_wrong_password**: Тестирует неудачную регистрацию с неправильным паролем.

### test_login_page.py

- **test_login_from_main_page**: Тестирует функцию входа с главной страницы.
- **test_login_from_personal_account**: Тестирует функцию входа с личного кабинета.
- **test_login_from_registration_page**: Тестирует функцию входа с страницы регистрации.
- **test_login_from_forgot_password_page**: Тестирует функцию входа с страницы восстановления пароля.

### test_transitions_between_sections.py

- **test_transition_to_personal_account**: Проверяет переход на страницу личного кабинета после входа с главной страницы.
- **test_transition_to_constructor_page**: Проверяет переход на страницу конструктора после входа.
- **test_transition_to_constructor_page_by_clicking_on_the_logo**: Проверяет переход на главную страницу после входа по клику на логотип.

### test_logout.py

- **test_logout**: Проверяет функцию выхода из системы.

### test_constructor_section.py

- **test_transition_between_sections**: Проверяет переход между вкладками "Соусы", "Начинки" и "Булки".




