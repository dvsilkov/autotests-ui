from playwright.sync_api import sync_playwright, expect  # Импорт Playwright для синхронного режима и проверки

# Запуск Playwright в синхронном режиме
with sync_playwright() as pw:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()  # Создаем новую страницу

    # Переходим на страницу авторизации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Находим поле "Email" и заполняем его
    registration_email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    registration_email_input.fill("user.name@gmail.com")

    # Находим поле "Username" и заполняем его
    registration_username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    registration_username_input.fill("username")

    # Находим поле "Password" и заполняем его
    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    password_input.fill("password")

    # Находим кнопку "Registration" и кликаем на нее
    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    # Проверяем, что на странице "Dashboard" отображается заголовок "Dashboard"
    dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(dashboard_title).to_be_visible()  # Проверяем видимость элемента
    expect(dashboard_title).to_have_text("Dashboard")  # Проверяем текст

    # Пауза на 1 секунду, чтобы увидеть результат
    page.wait_for_timeout(1000)