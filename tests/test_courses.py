import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    # Открываем браузер с использованием Playwright
    with sync_playwright() as pw:
        # Запускаем Chromium браузер в обычном режиме (не headless)
        browser = pw.chromium.launch(headless=False)
        # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
        context = browser.new_context()
        # Открываем новую страницу в рамках контекста
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

    # Открываем браузер с использованием сохраненного контекста
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Проверяем заголовок
        title_courses = page.get_by_test_id("courses-list-toolbar-title-text")
        expect(title_courses).to_be_visible()
        expect(title_courses).to_have_text("Courses")

        # Проверяем наличие и текст блока "There is no results"
        text_no_results = page.get_by_test_id("courses-list-empty-view-title-text")
        expect(text_no_results).to_be_visible()
        expect(text_no_results).to_have_text("There is no results")

        # Проверяем наличие и видимость иконки пустого блока
        icon_no_results = page.get_by_test_id("courses-list-empty-view-icon")
        expect(text_no_results).to_be_visible()

        # Проверяем наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
        text_no_results_description = page.get_by_test_id("courses-list-empty-view-description-text")
        expect(text_no_results_description).to_be_visible()
        expect(text_no_results_description).to_have_text("Results from the load test pipeline will be displayed here")

        page.wait_for_timeout(1000)