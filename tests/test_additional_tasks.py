from tasks.additional_tasks import factorial
from tasks.additional_tasks import power
from tasks.additional_tasks import sum_numbers


def test_regression_0():
    assert factorial(3) == 6
    assert factorial(5) == 120


def test_regression_1():
    assert power(2, 5) == 32
    assert power(5, 3) == 125


def test_regression_2():
    assert sum_numbers(12) == 3
    assert sum_numbers(9999) == 36
