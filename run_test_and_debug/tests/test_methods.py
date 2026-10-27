from src.calculation import sum_numbers, diff_numbers, multiply_numbers, square_numbers, divide_numbers, modulo_numbers
import pytest

def test_sum_numbers():
    assert sum_numbers(2, 3) == 5

def test_diff_numbers():
    assert diff_numbers(6, 4) == 2

def test_multiply_numbers():
    assert multiply_numbers(2, 3) == 6

def test_square_numbers():
    assert square_numbers(6) == 36

def test_modul0_numbers():
    assert modulo_numbers(6, 3) == 0

@pytest.mark.skip(reason = 'Flaky application test - to be addressed in ticket bug-1234')
def test_divide_numbers():
    assert divide_numbers(10, 5) == 2

@pytest.mark.xfail(reason = 'Flaky application test - to be addressed in ticket bug-1234')
def test_divide_numbers_again():
    assert divide_numbers(12, 3) == 4
