from tasks.task_22 import SherlockValidString


def test_regression():
    assert SherlockValidString("xyz") is True
    assert SherlockValidString("xyzaa") is True
    assert SherlockValidString("xxyyz") is True
    assert SherlockValidString("xyzzz") is False
    assert SherlockValidString("xxyyza") is False
    assert SherlockValidString("xxyyzabc") is False
