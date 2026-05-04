from playwright.sync_api import Page, expect

from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage

class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page) # Инициализация родительского класса

        # Добавляем компонент Navbar, вместо локаторов реализован как PageComponent
        self.navbar = NavbarComponent(page)
        # Добавляем компонент Sidebar, вместо локаторов реализован как PageComponent
        self.sidebar = SidebarComponent(page)
        # Добавляем компонент CourseView, вместо локаторов реализован как PageComponent
        self.course_view = CourseViewComponent(page)
        # Добавляем компонент EmptyView, пустой блок когда нет курсов, вместо локаторов реализован как PageComponent
        self.empty_view = EmptyViewComponent(page, 'courses-list')
        # Добавляем компонент ToolbarView, панель инструментов, вместо локаторов реализован как PageComponent
        self.toolbar_view = CoursesListToolbarViewComponent(page)

    def check_visible_empty_view(self):
        """
        проверяет наличие и видимость иконки, заголовка и описания пустого блока
        метод реализован через PageComponent
        """
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )
