from tasks.task_24 import MatrixTurn


def test_regression():
    Matrix = ["123456", "234567", "345678", "456789"]
    MatrixTurn(Matrix, 4, 6, 1)
    assert Matrix == ["212345", "343456", "456767", "567898"]
