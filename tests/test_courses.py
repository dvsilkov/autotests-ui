import pytest
from playwright.sync_api import expect

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем заголовок
    title_courses = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(title_courses).to_be_visible()
    expect(title_courses).to_have_text("Courses")

    # Проверяем наличие и текст блока "There is no results"
    text_no_results = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(text_no_results).to_be_visible()
    expect(text_no_results).to_have_text("There is no results")

    # Проверяем наличие и видимость иконки пустого блока
    icon_no_results = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(text_no_results).to_be_visible()

    # Проверяем наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
    text_no_results_description = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(text_no_results_description).to_be_visible()
    expect(text_no_results_description).to_have_text("Results from the load test pipeline will be displayed here")

    chromium_page_with_state.wait_for_timeout(1000)

# команда для запуска python -m pytest -v -s -m courses