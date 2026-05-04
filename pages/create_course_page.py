from playwright.sync_api import Page, expect

from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage

class CreateCoursePage(BasePage):
    """Класс с методами для страницы CreateCoursePage"""
    def __init__(self, page: Page):
        super().__init__(page)

        # Компонент, включающий в себя виджет по загрузке изображения. Вместо локаторов реализован как PageComponent
        # Компонент ImageUploadWidgetComponent также включает в себя компонент EmptyViewComponent
        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')

        # Блок, который отображается, когда в курсе нет заданий. Вместо локаторов реализован как PageComponent
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')

        # Компонент - форма для создания и редактирования заданий. Вместо локаторов реализован как PageComponent
        self.create_exercise_form = CreateCourseExerciseFormComponent(page)

        # Заголовок и кнопка создания курса
        self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

        # Форма создания курса
        self.create_course_title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.create_course_estimated_time_input = (
            page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        )
        self.create_course_description_textarea = (
            # При поиске поля описания будет найдено два тега textarea, берем первый из них
            page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        )
        self.create_course_max_score_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.create_course_min_score_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')

        # Заголовок и кнопка создания задания
        self.exercises_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.create_exercise_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

    # Методы для работы с заголовком и кнопкой создания курса:
    def check_visible_create_course_title(self):
        """проверяет наличие заголовка 'Create course'"""
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text('Create course')

    def click_create_course_button(self):
        """нажимает на кнопку создания курса"""
        self.create_course_button.click()

    def check_visible_create_course_button(self):
        """проверяет, что кнопка создания курса видна """
        expect(self.create_course_button).to_be_visible()

    def check_disabled_create_course_button(self):
        """проверяет, что кнопка создания курса неактивна """
        expect(self.create_course_button).to_be_disabled()

    # Методы для работы с формой создания курса:
    def check_visible_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        """проверяет наличие полей формы и их значения """
        expect(self.create_course_title_input).to_be_visible()
        expect(self.create_course_title_input).to_have_value(title)

        expect(self.create_course_estimated_time_input).to_be_visible()
        expect(self.create_course_estimated_time_input).to_have_value(estimated_time)

        expect(self.create_course_description_textarea).to_be_visible()
        expect(self.create_course_description_textarea).to_have_value(description)

        expect(self.create_course_max_score_input).to_be_visible()
        expect(self.create_course_max_score_input).to_have_value(max_score)

        expect(self.create_course_min_score_input).to_be_visible()
        expect(self.create_course_min_score_input).to_have_value(min_score)

    def fill_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        """заполняет форму создания курса """
        self.create_course_title_input.fill(title)
        expect(self.create_course_title_input).to_have_value(title)

        self.create_course_estimated_time_input.fill(estimated_time)
        expect(self.create_course_estimated_time_input).to_have_value(estimated_time)

        self.create_course_description_textarea.fill(description)
        expect(self.create_course_description_textarea).to_have_value(description)

        self.create_course_max_score_input.fill(max_score)
        expect(self.create_course_max_score_input).to_have_value(max_score)

        self.create_course_min_score_input.fill(min_score)
        expect(self.create_course_min_score_input).to_have_value(min_score)

    # Методы для работы с упражнениями
    def check_visible_exercises_title(self):
        """проверяет наличие заголовка 'Exercises' """
        expect(self.exercises_title).to_be_visible()
        expect(self.exercises_title).to_have_text('Exercises')

    def check_visible_create_exercise_button(self):
        """проверяет наличие кнопки создания упражнения """
        expect(self.create_exercise_button).to_be_visible()

    def click_create_exercise_button(self):
        """нажимает на кнопку создания упражнения """
        self.create_exercise_button.click()

    def check_visible_exercises_empty_view(self):
        """
        проверяет, что отображается пустой блок для заданий, когда нет заданий в курсе
        метод реализован через PageComponent
        """
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )