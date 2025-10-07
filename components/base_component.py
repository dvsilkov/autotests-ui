from playwright.sync_api import Page, expect
from typing import Pattern

class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]): # Pattern[str] — это скомпилированное регулярное выражение
        """метод проверяет, что текущий URL страницы соответствует регулярному выражению expected_url
        пример вызова метода self.check_current_url(re.compile(r".*/#/dashboard"))
        """
        expect(self.page).to_have_url(expected_url)