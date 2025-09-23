from tasks.task_28 import Keymaker


def test_regression():
    assert Keymaker(1) == "1"
    assert Keymaker(2) == "10"
    assert Keymaker(4) == "1001"
    assert Keymaker(8) == "10010000"
    assert Keymaker(9) == "100100001"
