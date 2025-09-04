from tasks.task_15 import TankRush


def test_regression():
    test_H1 = 3
    test_W1 = 4
    test_S1 = "1234 2345 0987"
    test_H2 = 2
    test_W2 = 2
    test_S2 = "34 98"
    assert TankRush(test_H1, test_W1, test_S1, test_H2, test_W2, test_S2) is True


def test_regression2():
    test_H1 = 3
    test_W1 = 4
    test_S1 = "1234 2345 0987"
    test_H2 = 3
    test_W2 = 3
    test_S2 = "234 345 987"
    assert TankRush(test_H1, test_W1, test_S1, test_H2, test_W2, test_S2) is True


def test_regression3():
    test_H1 = 3
    test_W1 = 4
    test_S1 = "1234 2345 0987"
    test_H2 = 2
    test_W2 = 2
    test_S2 = "35 98"
    assert TankRush(test_H1, test_W1, test_S1, test_H2, test_W2, test_S2) is False


def test_regression4():
    test_H1 = 3
    test_W1 = 4
    test_S1 = "1234 2345 0987"
    test_H2 = 2
    test_W2 = 2
    test_S2 = "34 91"
    assert TankRush(test_H1, test_W1, test_S1, test_H2, test_W2, test_S2) is False


def test_regression5():
    test_H1 = 3
    test_W1 = 4
    test_S1 = "1234 2345 0987"
    test_H2 = 1
    test_W2 = 2
    test_S2 = "34"
    assert TankRush(test_H1, test_W1, test_S1, test_H2, test_W2, test_S2) is True


def test_regression6():
    test_H1 = 3
    test_W1 = 4
    test_S1 = "1234 2345 0987"
    test_H2 = 2
    test_W2 = 2
    test_S2 = "34 45"
    assert TankRush(test_H1, test_W1, test_S1, test_H2, test_W2, test_S2) is True


def test_regression7():
    test_H1 = 2
    test_W1 = 4
    test_S1 = "1111 1112"
    test_H2 = 2
    test_W2 = 2
    test_S2 = "11 12"
    assert TankRush(test_H1, test_W1, test_S1, test_H2, test_W2, test_S2) is True


def test_regression8():
    test_H1 = 2
    test_W1 = 2
    test_S1 = "11 11"
    test_H2 = 2
    test_W2 = 2
    test_S2 = "11 11"
    assert TankRush(test_H1, test_W1, test_S1, test_H2, test_W2, test_S2) is True
    
def test_regression9():
    test_H1 = 5
    test_W1 = 15
    test_S1 = "000000000000000 000000000000000 000000100000000 000000000000000 000000000000000"
    test_H2 = 3
    test_W2 = 5
    test_S2 = "00000 00000 00001"
    assert TankRush(test_H1, test_W1, test_S1, test_H2, test_W2, test_S2) is True
