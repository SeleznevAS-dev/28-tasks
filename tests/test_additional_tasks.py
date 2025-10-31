import pytest
import random

from tasks.additional_tasks import factorial
from tasks.additional_tasks import power
from tasks.additional_tasks import sum_numbers
from tasks.additional_tasks import list_len
from tasks.additional_tasks import is_palindrome
from tasks.additional_tasks import find_second_max
from tasks.additional_tasks import generate_parens


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
    assert is_palindrome("aba") is True
    assert is_palindrome("abc") is False
    assert is_palindrome("abccba") is True
    assert is_palindrome("abccbb") is False


@pytest.mark.repeat(100)
def test_random_second_max():
    arr = []
    for _ in range(100):
        arr.append(random.randint(1, 100))
    test_arr = arr.copy()
    mx = max(arr)
    arr.remove(mx)

    assert find_second_max(test_arr) == max(arr)


def test_regression_5():
    assert generate_parens(1) == ["()"]
    assert generate_parens(2) == ["(())", "()()"]
    assert generate_parens(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
