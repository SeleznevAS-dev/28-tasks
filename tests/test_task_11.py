from tasks.task_11 import BigMinus
import pytest
from random import randint


def test_regression():
    test_s1 = "1234567891"
    test_s2 = "1"
    assert BigMinus(test_s1, test_s2) == "1234567890"


def test_regression2():
    test_s1 = "1"
    test_s2 = "321"
    assert BigMinus(test_s1, test_s2) == "320"


@pytest.mark.repeat(1000)
def test_random():
    test_s1 = str(randint(1, 1000))
    test_s2 = str(randint(1, 1000))
    assert BigMinus(test_s1, test_s2) == str(abs(int(test_s1) - int(test_s2)))
