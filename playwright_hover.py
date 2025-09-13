from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Находим ссылку Registration
    registration_link = page.get_by_test_id('login-page-registration-link')

    # Получаем стиль до наведения с помощью JS
    initial_text_decoration = registration_link.evaluate("el => window.getComputedStyle(el).textDecoration")

    # Выполняем наведение курсора на ссылку
    registration_link.hover()

    # Получаем стиль после наведения с помощью JS
    hovered_text_decoration = registration_link.evaluate("el => window.getComputedStyle(el).textDecoration")

    # Проверяем изменение
    assert 'underline' in hovered_text_decoration, "Текст не стал подчеркнутым при наведении"
    assert initial_text_decoration != hovered_text_decoration, "Стиль не изменился при наведении"

    # Добавляем паузу для наглядности результата
    page.wait_for_timeout(1000)