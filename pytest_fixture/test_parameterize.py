import pytest


@pytest.mark.parametrize(
    ("actual_message", "expected_message"),
    [
        ("Invalid password", "Invalid password"),
        ("Please check your password", "Please check your password"),
        ("valid password", "valid password"),
        ("login-successfull", "login-successfull"),

    ],
)
def test_error_message(actual_message, expected_message):
    assert actual_message == expected_message