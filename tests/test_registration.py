import pytest
from pages.registration_page import RegistrationPage # Импортируем класс RegistrationPage
from pages.dashboard_page import DashboardPage # Импортируем класс DashboardPage

@pytest.mark.regression
@pytest.mark.registration
# в аргументах метода указываем фикстуры registration_page и dashboard_page, которые инициализируют страницы
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    """ Проверка успешной регистрации """
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_registration_form(email='user@gmail.com', username='username', password='password')
    registration_page.click_registration_button()
    dashboard_page.check_visible_dashboard_title(title_text="Dashboard")

# команда для запуска python -m pytest -k "test_registration" -s -v