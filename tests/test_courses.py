import pytest
from playwright.sync_api import expect, Page
from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    """тест проверяет элементы на странице Courses без добавленных курсов"""

    # переходим на страницу
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    #   проверка Navbar компонента на странице CoursesListPage
    courses_list_page.navbar.check_visible("username")

    # проверка Sidebar компонента на странице CoursesListPage
    courses_list_page.sidebar.check_visible()

    # проверка Toolbar компонента на странице CoursesListPage (заголовок и кнопка добавления курса)
    courses_list_page.toolbar_view.check_visible()

    # Проверяем наличие и видимость иконки, заголовка и описания пустого блока
    courses_list_page.check_visible_empty_view()

# команда для запуска python -m pytest -k "test_empty_courses_list" -s -v

@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    """тест проверяет форму создания курса, создает курс и проверяет форму списка курсов с добавленным курсом"""
    # Открыть ссылку
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    # Проверить наличие заголовка "Create course"
    create_course_page.check_visible_create_course_title()
    # Проверить, что кнопка создания курса недоступна для нажатия
    create_course_page.check_disabled_create_course_button()
    # Проверить отображение пустого блока для превью изображения и что в блоке загрузки изображения картинка не выбрана
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
    # Проверить, что форма создания курса отображается и содержит значения по умолчанию
    create_course_page.check_visible_create_course_form(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0"
    )
    # Проверить наличие заголовка "Exercises"
    create_course_page.check_visible_exercises_title()
    # Проверить наличие кнопки создания задания
    create_course_page.check_visible_create_exercise_button()
    # Убедиться, что отображается блок с пустыми заданиями
    create_course_page.check_visible_exercises_empty_view()
    # Загрузить изображение для превью курса и проверить блок загрузки изображения, когда картинка успешно загружена
    create_course_page.image_upload_widget.upload_preview_image(file='./testdata/files/image.png')
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

    # Заполнить форму создания курса значениями
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )
    # Нажать на кнопку создания курса. После создания курса произойдет редирект на страницу с курсами
    create_course_page.click_create_course_button()

    # проверка Toolbar компонента на странице CoursesListPage (заголовок и кнопка добавления курса)
    courses_list_page.toolbar_view.check_visible()

    # Проверить корректность отображаемых данных на карточке курса
    courses_list_page.course_view.check_visible(
        index=0,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks"
    )

# команда для запуска python -m pytest -k "test_create_course" -s -v