import random
import pytest
from tasks.task_2 import odometer


@pytest.mark.repeat(100)
def test_regression_and_random():
    random_n = random.randint(1, 100)
    test_res = 0
    test_arr = []
    for _ in range(random_n):
        for j in range(2):
            num = random.randint(1, 50)
            if j == 0:
                test_res += num
            test_arr.append(num)
    assert odometer(test_arr) == test_res


def test_min_max():
    arr_min = [0, 0]
    arr_max = [10**20, 10**20]
    test_res_min = 0
    test_res_max = 10**20
    test_res_min = arr_min[0]
    test_res_max = arr_max[0]
    assert odometer(arr_min) == test_res_min
    assert odometer(arr_max) == test_res_max
