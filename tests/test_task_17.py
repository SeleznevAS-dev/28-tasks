from tasks.task_17 import LineAnalysis


def test_regression():
    test_line = "*..*..*..*..*..*..*"
    assert LineAnalysis(test_line) is True


def test_regression2():
    test_line = "*..*...*..*..*..*..*"
    assert LineAnalysis(test_line) is False


def test_regression3():
    test_line = "*"
    assert LineAnalysis(test_line) is True
