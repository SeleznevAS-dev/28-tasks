from tasks.task_25 import TransformTransform


def test_regression():
    assert TransformTransform([1, 2, 3], 3) is True
    assert TransformTransform([1, 2, 3, 4], 4) is False
    assert TransformTransform([1, 2, 1, 7, 2, 4, 3, 1, 5, 1, 2, 1, 6, 1, 2], 15) is False