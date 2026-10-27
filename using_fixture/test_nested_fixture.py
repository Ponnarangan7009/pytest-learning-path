import pytest

@pytest.fixture
def first_name():
    return "john"

@pytest.fixture
def last_name():
    return "smith"

@pytest.fixture
def age():
    return 26

@pytest.fixture
def person(first_name, last_name, age):
    return f"{first_name} {last_name} is {age} years old."


def test_check_person_details(person):
    assert person == "john smith is 26 years old."

def test_age(person):
    assert "26" in person

def test_last_name(person):
    assert "smith" in person
