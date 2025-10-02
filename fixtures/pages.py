import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

@pytest.fixture
# метод в качестве аргумента принимает фикстуру chromium_page, которая открывает браузер и создает страницу
def login_page(chromium_page: Page) -> LoginPage:
    """ Фикстура для инициализации страницы LoginPage, возвращает экземпляр класса """
    return LoginPage(page=chromium_page)

@pytest.fixture
# метод в качестве аргумента принимает фикстуру chromium_page, которая открывает браузер и создает страницу
def registration_page(chromium_page: Page) -> RegistrationPage:
    """ Фикстура для инициализации страницы RegistrationPage, возвращает экземпляр класса"""
    return RegistrationPage(page=chromium_page)

@pytest.fixture
# метод в качестве аргумента принимает фикстуру chromium_page, которая открывает браузер и создает страницу
def dashboard_page(chromium_page: Page) -> DashboardPage:
    """ Фикстура для инициализации страницы DashboardPage, возвращает экземпляр класса"""
    return DashboardPage(page=chromium_page)

@pytest.fixture
# в качестве аргумента фикстура chromium_page_with_state, позволяет сразу открывать нужную страницу, без авторизации
def courses_list_page(chromium_page_with_state: Page) -> CoursesListPage:
    """ Фикстура для инициализации страницы CoursesListPage, возвращает экземпляр класса"""
    return CoursesListPage(page=chromium_page_with_state)

@pytest.fixture
# в качестве аргумента фикстура chromium_page_with_state, позволяет сразу открывать нужную страницу, без авторизации
def create_course_page(chromium_page_with_state: Page) -> CreateCoursePage:
    """ Фикстура для инициализации страницы CreateCoursePage, возвращает экземпляр класса"""
    return CreateCoursePage(page=chromium_page_with_state)