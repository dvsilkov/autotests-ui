import pytest

from pages.dashboard_page import DashboardPage

@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard_displaying(dashboard_page_with_state: DashboardPage):

    # переходим на страницу
    dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    #  проверка Navbar компонента на странице DashboardPage
    dashboard_page_with_state.navbar.check_visible("username")

    #  проверка Sidebar компонента на странице DashboardPage
    dashboard_page_with_state.sidebar.check_visible()

    # остальные шаги теста с методами для DashboardPage
    dashboard_page_with_state.check_visible_dashboard_title("Dashboard")
    dashboard_page_with_state.check_visible_scores_chart()
    dashboard_page_with_state.check_visible_courses_chart()
    dashboard_page_with_state.check_visible_students_chart()
    dashboard_page_with_state.check_visible_activities_chart()

# команда для запуска python -m pytest -k "test_dashboard_displaying" -s -v