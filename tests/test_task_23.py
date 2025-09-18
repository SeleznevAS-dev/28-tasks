from tasks.task_23 import TreeOfLife


def test_regression():
    assert TreeOfLife(3, 4, 12, [".+..", "..+.", ".+.."]) == [".+..", "..+.", ".+.."]
    assert TreeOfLife(3, 4, 1, [".+..", "..+.", ".+.."]) == ["++++", "++++", "++++"]
    assert TreeOfLife(3, 3, 2, ["+++", "+++", "+++"]) == ["...", "...", "..."]
