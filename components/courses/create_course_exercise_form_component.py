from components.base_component import BaseComponent, expect

class CreateCourseExerciseFormComponent(BaseComponent):
    """
    Класс описывает компонент, который представляет собой форму для создания и редактирования заданий. Содержит локаторы
    и методы для работы с компонентом
    компонент включает следующие элементы:
    subtitle — подзаголовок задания с текстом #{index+1} Exercise
    title_input — поле для ввода заголовка задания
    description_input — поле для ввода описания задания
    delete_button — кнопка для удаления задания
    Все эти локаторы динамические, и в них подставляется index
    """
    def click_delete_button(self, index: int):
        """
        Метод для удаления упражнения
        """
        delete_button = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-delete-exercise-button"
        )
        delete_button.click()

    def check_visible(self, index: int, title: str, description: str):
        """
        Метод проверяет форму редактирования упражнения с учетом индекса упражнения
        """
        subtitle = self.page.get_by_test_id(f"create-course-exercise-{index}-box-toolbar-subtitle-text")
        title_input = self.page.get_by_test_id(f"create-course-exercise-form-title-{index}-input")
        description_input = self.page.get_by_test_id(f"create-course-exercise-form-description-{index}-input")

        expect(subtitle).to_be_visible()
        expect(subtitle).to_have_text(f"#{index + 1} Exercise")

        expect(title_input).to_be_visible()
        expect(title_input).to_have_value(title)

        expect(description_input).to_be_visible()
        expect(description_input).to_have_value(description)

    def fill(self, index: int, title: str, description: str):
        """
        Метод заполняет форму редактирования упражнения
        """
        title_input = self.page.get_by_test_id(f"create-course-exercise-form-title-{index}-input")
        description_input = self.page.get_by_test_id(f"create-course-exercise-form-description-{index}-input")

        title_input.fill(title)
        expect(title_input).to_have_value(title)

        description_input.fill(description)
        expect(description_input).to_have_value(description)