from tasks.task_4 import MadMax


def test_regression():
    test_N = 7
    test_Tele = [1, 2, 3, 4, 5, 6, 7]
    assert MadMax(test_N, test_Tele) == [1, 2, 3, 7, 6, 5, 4]
