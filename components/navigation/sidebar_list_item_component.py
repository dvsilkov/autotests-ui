from typing import Pattern
from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

class SidebarListItemComponent(BaseComponent):
    """ Класс описывает три кнопки в SidebarComponent"""
    # передаем identifier в конструктор класса, чтобы динамически создавать локаторы
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        # компонент SidebarListItemComponent состоит из трех элементов: icon, title, и button,
        # следовательно, нам нужно будет три локатора, которые формируем динамически
        self.icon = page.get_by_test_id(f'{identifier}-drawer-list-item-icon')
        self.title = page.get_by_test_id(f'{identifier}-drawer-list-item-title-text')
        self.button = page.get_by_test_id(f'{identifier}-drawer-list-item-button')

    # методы для работы с каждым элементом в SidebarComponent
    def check_visible(self, title: str):
        """ проверяет, что компонент отображается корректно на странице. Он проверяет наличие и видимость icon,
        title (включая текст), и button
        """
        expect(self.icon).to_be_visible()

        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)

        expect(self.button).to_be_visible()

    def navigate(self, expected_url: Pattern[str]):
        """ выполняет клик на button и проверяет, что редирект произошел на нужную страницу"""
        self.button.click()
        self.check_current_url(expected_url)