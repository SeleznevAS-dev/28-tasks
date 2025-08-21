from tasks.task_8 import SumOfThe


def test_regression():
    test_N = 7
    test_data = [100, -50, 10, -25, 90, -35, 90]
    assert SumOfThe(test_N, test_data) == 90


def test_regression2():
    test_N = 5
    test_data = [5, -25, 10, -35, -45]
    assert SumOfThe(test_N, test_data) == -45
