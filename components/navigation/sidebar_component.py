import re
from  playwright.sync_api import Page
from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent

class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # создаем экземпляры для каждого компонента Sidebar
        self.logout_list_item = SidebarListItemComponent(page, 'logout')
        self.courses_list_item = SidebarListItemComponent(page, 'courses')
        self.dashboard_list_item = SidebarListItemComponent(page, 'dashboard')

    # методы для проверки компонентов Sidebar
    def check_visible(self):
        """
        этот метод будет проверять корректное отображение компонента Sidebar.
        Мы проверим, что все элементы Sidebar видны на странице
        """
        self.logout_list_item.check_visible('Logout')
        self.courses_list_item.check_visible('Courses')
        self.dashboard_list_item.check_visible('Dashboard')

    def click_logout(self):
        """
        этот метод будет имитировать нажатие на элемент выхода из приложения (Logout)
        и проверять, что произошел редирект на URL /#/auth/login
        """
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"))

    def click_courses(self):
        """
        этот метод будет имитировать нажатие на элемент перехода к курсам (Courses)
        и проверять, что произошел редирект на URL /#/courses
        """
        self.courses_list_item.navigate(re.compile(r".*/#/courses"))

    def click_dashboard(self):
        """
        этот метод будет имитировать нажатие на элемент перехода на панель управления (Dashboard)
        и проверять, что произошел редирект на URL /#/dashboard
        """
        self.dashboard_list_item.navigate(re.compile(r".*/#/dashboard"))