from tasks.task_27 import Football


def test_regression():
    assert Football([1, 3, 2], 3) is True
    assert Football([3, 2, 1], 3) is True
    assert Football([1, 7, 5, 3, 9], 5) is True
    assert Football([9, 5, 3, 7, 1], 5) is False
    assert Football([1, 4, 3, 2, 5], 5) is True
    assert Football([1, 5, 4, 3, 2], 5) is True
