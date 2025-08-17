from tasks.task_6 import PatternUnlock


def test_regression():
    test_N = 10
    test_hits = [1, 2, 3, 4, 5, 6, 2, 7, 8, 9]
    assert PatternUnlock(test_N, test_hits) == "982843"
