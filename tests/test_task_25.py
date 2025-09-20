from tasks.task_25 import TransformTransform


def test_regression():
    assert TransformTransform([1, 2, 3], 3) is False
    assert TransformTransform([1, 2, 3, 4], 4) is True
