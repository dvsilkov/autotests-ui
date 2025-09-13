from playwright.sync_api import sync_playwright, expect

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Находим кнопку регистрации
    registration_button = page.get_by_test_id("registration-page-registration-button")

    # Проверяем, что кнопка не активна
    expect(registration_button).to_be_disabled()

    # Находим поле "Email" и заполняем его
    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    email_input.fill("user.name@gmail.com")

    # Находим поле "Username" и заполняем его
    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    username_input.type("username", delay=100)

    # Находим поле "Password" и заполняем его
    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    password_input.fill("password")

    # Проверяем, что кнопка активна
    expect(registration_button).not_to_be_disabled()