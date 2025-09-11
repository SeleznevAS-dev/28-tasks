from tasks.task_19 import ShopOLAP


def test_regression():
    test_N = 5
    test_items = ["платье1 5", "сумка32 2", "платье1 1", "сумка23 2", "сумка128 4"]
    assert ShopOLAP(test_N, test_items) == [
        "платье1 6",
        "сумка128 4",
        "сумка23 2",
        "сумка32 2",
    ]

def test_regression2():
    test_N = 4
    test_items = ["платье1 2", "сумка32 2", "сумка23 2", "сумка128 2"]
    assert ShopOLAP(test_N, test_items) == [
        "платье1 2",
        "сумка128 2",
        "сумка23 2",
        "сумка32 2",
    ]