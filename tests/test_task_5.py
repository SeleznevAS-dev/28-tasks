from tasks.task_5 import SynchronizingTables


def test_regression():
    test_N = 3
    test_ids = [50, 1, 1024]
    test_salary = [20000, 100000, 90000]
    assert SynchronizingTables(test_N, test_ids, test_salary) == [90000, 20000, 100000]

def test_regression2():
    test_N = 7
    test_ids = [50, 1, 1024, 2, 3, 4, 5]
    test_salary = [20000, 20000, 20000, 20000, 20000, 100000, 90000]
    assert SynchronizingTables(test_N, test_ids, test_salary) == [
        90000,
        20000,
        100000,
        20000,
        20000,
        20000,
        20000,
    ]