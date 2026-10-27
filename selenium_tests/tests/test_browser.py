from pages.web_form_page import WebFormPage
import pytest


@pytest.mark.smoke
def test_web_form_has_text_field(driver):
    page = WebFormPage(driver)
    page.open()
    assert page.is_text_field_displayed()


@pytest.mark.regression
def test_text_field_accepts_input(driver):
    page = WebFormPage(driver)
    page.open()
    page.enter_text("pytest-learner")
    field_value = page.get_text_field_value()

    assert field_value == "pytest-learner"


@pytest.mark.regression
@pytest.mark.parametrize(
    ("user_input", "expected_message"),
    [
        ("pytest learner", "Received!"),
        ("Selenium", "Received!"),
    ],
)
def test_submit_form(driver, user_input, expected_message):
    page = WebFormPage(driver)
    page.open()
    page.enter_text(user_input)
    page.submit()

    assert page.get_message() == expected_message