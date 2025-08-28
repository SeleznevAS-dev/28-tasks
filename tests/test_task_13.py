from tasks.task_13 import UFO


def test_regression():
    test_N = 2
    test_data = [1234, 1777]
    test_octal = False
    assert UFO(test_N, test_data, test_octal) == [4660, 6007]


def test_regression2():
    test_N = 2
    test_data = [1234, 1777]
    test_octal = True
    assert UFO(test_N, test_data, test_octal) == [668, 1023]
