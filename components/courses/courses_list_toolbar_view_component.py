import re

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CoursesListToolbarViewComponent(BaseComponent):
    """
    Класс описывает элементы в компоненте CoursesListToolbarViewComponent (панель инструментов для работы с курсами)
    Этот компонент можно будет многократно использовать в различных автотестах
    """
    def __init__(self, page: Page):
        super().__init__(page)

        # локаторы для CoursesListToolbarViewComponent
        self.title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

    def check_visible(self):
        """ проверяет видимость заголовка в панели инструментов """
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Courses')

        expect(self.create_course_button).to_be_visible()

    def click_create_course_button(self):
        """ проверяет видимость кнопки для создания нового курса """
        self.create_course_button.click()
        # Дополнительно проверим, что произошел редирект на правильную страницу
        self.check_current_url(re.compile(".*/#/courses/create"))