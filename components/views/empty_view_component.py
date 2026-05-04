from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

class EmptyViewComponent(BaseComponent):
    """
    Класс описывает общие элементы в компоненте EmptyViewComponent
    Этот компонент можно будет многократно использовать в различных автотестах, где встречается
    пустой вид (например, на страницах со списками курсов и страницах создания курсов)
    """

    # передаем identifier в конструктор класса, чтобы динамически создавать локаторы
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        # локаторы для EmptyViewComponent
        # локаторов будет всего три: icon, title, и description в виде шаблона {identifier}-empty-view-{element}
        self.icon = page.get_by_test_id(f'{identifier}-empty-view-icon')
        self.title = page.get_by_test_id(f'{identifier}-empty-view-title-text')
        self.description = page.get_by_test_id(f'{identifier}-empty-view-description-text')

    def check_visible(self, title: str, description: str):
        """
        метод для проверки видимости элементов в EmptyViewComponent
        на входе принимает аргументы со значениями заголовка и описания
        """
        # Проверяем видимость иконки
        expect(self.icon).to_be_visible()

        # Проверяем видимость заголовка и его текст
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)

        # Проверяем видимость описания и его текст
        expect(self.description).to_be_visible()
        expect(self.description).to_have_text(description)