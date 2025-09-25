import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    """ Фикстура для инициализции страницв LoginPage, возвращает экземпляр класса """
    return LoginPage(page=chromium_page)

@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    """ Фикстура для инициализции страницв RegistrationPage, возвращает экземпляр класса"""
    return RegistrationPage(page=chromium_page)

@pytest.fixture
def dashboard_page(chromium_page: Page) -> DashboardPage:
    """ Фикстура для инициализции страницв DashboardPage, возвращает экземпляр класса"""
    return DashboardPage(page=chromium_page)