from tasks.task_14 import Unmanned


def test_regression():
    test_L = 10
    test_N = 2
    tesk_track = [[3, 5, 5], [5, 2, 2]]
    assert Unmanned(test_L, test_N, tesk_track) == 12

def test_regression2():
    test_L = 10
    test_N = 2
    tesk_track = [[11, 5, 5], [15, 2, 2]]
    assert Unmanned(test_L, test_N, tesk_track) == 10