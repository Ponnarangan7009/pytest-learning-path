import pytest

@pytest.fixture
def numbers_list():
    return [1, 2, 3, 4, 8]

def test_check_sum_numbers(numbers_list):
    sum_numbers = sum(numbers_list)

    assert sum_numbers == 18

def test_check_len_numbers(numbers_list):
    len_numbers = len(numbers_list)

    assert len_numbers == 5