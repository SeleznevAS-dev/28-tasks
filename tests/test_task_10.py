from tasks.task_10 import PrintingCosts


def test_regression():
    test_Line = "JP"
    assert PrintingCosts(test_Line) == 41


def test_regression2():
    test_Line = '"абв"'
    assert PrintingCosts(test_Line) == 81
