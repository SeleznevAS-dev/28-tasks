from tasks.task_7 import WordSearch


def test_regression():
    test_width = 12
    test_s = (
        "1) строка разбивается на набор строк через выравнивание по заданной ширине."
    )
    test_subs = "строк"
    assert WordSearch(test_width, test_s, test_subs) == [0, 0, 0, 1, 0, 0, 0]


def test_regression2():
    test_width = 3
    test_s = "12345"
    test_subs = "123"
    assert WordSearch(test_width, test_s, test_subs) == [1, 0]
