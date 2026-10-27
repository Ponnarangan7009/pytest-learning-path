import pytest

@pytest.fixture
def expected_error_message():
    return "Invalid password"

class TestLoginPage:

    def test_error_message_uses_fixture(self, expected_error_message):
        actual_message = "Invalid password"

        assert actual_message == expected_error_message

    def test_error_message_matches(self):
        actual_message = "Invalid password"
        expected_message = "Invalid password"

        assert actual_message == expected_message

    def test_page_title_is_expected(self):
        actual_title = "Online Store"
        expected_title = "Online Store"

        assert actual_title == expected_title