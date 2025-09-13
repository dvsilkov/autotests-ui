from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Устанавливаем фокус на поле Email
    email_input = page.get_by_test_id("login-form-email-input").locator("input")
    email_input.focus()

    # По символу имитируем нажатия клавиш для ввода текста и добавляем задержку 300 мс для имитации реального ввода
    page.keyboard.type("user@gmail.com", delay=300)

    # Выделяем весь текст в поле Email с помощью комбинации клавиш Ctrl+A
    page.keyboard.press("ControlOrMeta+A")

    # Нажимаем Shift
    page.keyboard.down("Shift")

    # С нажатым Shift нажимаем стрелку влево 3 раза, снимая выделение
    for i in range(3):
        page.keyboard.press("ArrowLeft")

    # Отжимаем Shift
    page.keyboard.up("Shift")

    # Удаляем оставшийся выделенный текст через нажатие кнопки Delete
    page.keyboard.press("Delete")

    # Ждём 1 секунду для наглядности результата
    page.wait_for_timeout(1000)

    # Заполняем поле через метод fill
    email_input.fill("user@gmail.com")

    # Ждём 1 секунду для наглядности результата
    page.wait_for_timeout(1000)