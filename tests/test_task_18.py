from tasks.task_18 import MisterRobot


def test_regression():
    test_N = 7
    test_data = [1, 3, 4, 5, 6, 2, 7]
    assert MisterRobot(test_N, test_data) is True
