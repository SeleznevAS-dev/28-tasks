from tasks.task_16 import MaximumDiscount


def test_regression():
    test_N = 7
    test_price = [400, 350, 300, 250, 200, 150, 100]
    assert MaximumDiscount(test_N, test_price) == 450
