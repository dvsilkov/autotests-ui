import pytest  # Импортируем pytest
from playwright.sync_api import sync_playwright, Page  # Импортируем класс страницы, для аннотации типов


import pytest  # Импортируем pytest
from playwright.sync_api import sync_playwright, \
    Page, Playwright  # Импортируем класс страницы и экземпляр Playwright


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def chromium_page() -> Page:  # Аннотируем возвращаемое фикстурой значение
    # Ниже идет инициализация и открытие новой страницы
    with sync_playwright() as playwright:
        # Запускаем браузер
        browser = playwright.chromium.launch(headless=False)
        # создаем контекст
        context = browser.new_context()
        # создаем страницу
        page = context.new_page()
        # Передаем страницу для использования в тесте
        yield page

        # Закрываем страницу, контекст и браузер после выполнения тестов
        page.close()
        context.close()
        browser.close()

# фикстура регистрирует нового пользователя и сохраняет состояние браузера для последующего использования
@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.type('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.type('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.type('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path="browser-state.json")

    page.wait_for_timeout(1000)

# фикстура открывает новую страницу браузера, используя сохраненное состояние из файла browser-state.json
@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()
