from tasks.task_23 import TreeOfLife


def test_regression():
    assert TreeOfLife(3, 4, 12, [".+..", "..+.", ".+.."]) == [".+..", "..+.", ".+.."]
