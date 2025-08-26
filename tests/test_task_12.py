from tasks.task_12 import MassVote


def test_regression():
    test_N = 5
    test_Votes = [60, 10, 10, 15, 5]
    assert MassVote(test_N, test_Votes) == "majority winner 1"


def test_regression2():
    test_N = 3
    test_Votes = [10, 15, 10]
    assert MassVote(test_N, test_Votes) == "minority winner 2"


def test_regression3():
    test_N = 4
    test_Votes = [111, 111, 110, 110]
    assert MassVote(test_N, test_Votes) == "no winner"


def test_regression4():
    test_N = 1
    test_Votes = [100]
    assert MassVote(test_N, test_Votes) == "majority winner 1"
