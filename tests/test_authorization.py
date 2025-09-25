import pytest
from pages.login_page import LoginPage # Импортируем LoginPage

@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("email, password", [
    ("user.name@gmail.com", "password"),
    ("user.name@gmail.com", "  "),
    ("  ", "password")
])

# Создаем тестовую функцию с параметрами
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    """ Проверка неуспешной авторизации """
    # с помощью метода visit, наследуемого от BasePage, открываем страницу авторизации
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Используем метод fill_login_form для заполнения полей логина и пароля
    login_page.fill_login_form(email=email, password=password)

    # Метод click_login_button позволит нам нажать на кнопку "Login"
    login_page.click_login_button()

    # Для проверки сообщения об ошибке используем метод check_visible_wrong_email_or_password_alert
    login_page.check_visible_wrong_email_or_password_alert()

# команда для запуска python -m pytest -k "test_wrong_email_or_password_authorization" -s -v
