from tasks.task_21 import BiggerGreater


def test_regression():
    assert BiggerGreater("ая") == "яа"
    assert BiggerGreater("fff") == ""
    assert BiggerGreater("нклм") == "нкмл"
    assert BiggerGreater("вибк") == "викб"
    assert BiggerGreater("вкиб") == "ибвк"
