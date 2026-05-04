from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CourseViewMenuComponent(BaseComponent):
    """
    Класс описывает элементы в компоненте CourseViewMenuComponent (меню в виде трех точек)
    Этот компонент можно будет многократно использовать в различных автотестах, где есть это меню
    """
    def __init__(self, page: Page):
        super().__init__(page)

        # локаторы для CourseViewMenuComponent
        self.menu_button = page.get_by_test_id('course-view-menu-button')
        self.edit_menu_item = page.get_by_test_id('course-view-edit-menu-item')
        self.delete_menu_item = page.get_by_test_id('course-view-delete-menu-item')

    #  методы для работы с курсами
    def click_edit(self, index: int):
        """
        нажимает на кнопку редактирования курса в меню
        принимает индекс элемента курса для работы с нужной карточкой (это важно, когда на странице несколько курсов)
        """
        self.menu_button.nth(index).click()

        expect(self.edit_menu_item.nth(index)).to_be_visible()
        self.edit_menu_item.nth(index).click()

    def click_delete(self, index: int):
        """ аналогично предыдущему методу, но удаляет курс """
        self.menu_button.nth(index).click()

        expect(self.delete_menu_item.nth(index)).to_be_visible()
        self.delete_menu_item.nth(index).click()