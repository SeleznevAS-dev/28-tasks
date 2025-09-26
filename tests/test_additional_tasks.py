from tasks.additional_tasks import factorial
from tasks.additional_tasks import power
from tasks.additional_tasks import sum_numbers
from tasks.additional_tasks import list_len
from tasks.additional_tasks import is_palindrome


def test_regression_0():
    assert factorial(3) == 6
    assert factorial(5) == 120


def test_regression_1():
    assert power(2, 5) == 32
    assert power(5, 3) == 125


def test_regression_2():
    assert sum_numbers(12) == 3
    assert sum_numbers(9999) == 36


def test_regression_3():
    assert list_len([1]) == 1
    assert list_len([1, 1, 1, 1, 1]) == 5


def test_regression_4():
    assert is_palindrome("aba", 3) is True
    assert is_palindrome("abc", 3) is False
    assert is_palindrome("abccba", 6) is True
    assert is_palindrome("abccbb", 6) is False
