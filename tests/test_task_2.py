import random
import pytest
from tasks.task_2 import odometer


def test_regression():
    test_arr = [20, 2, 30, 6, 10, 7]
    test_res = 170
    assert odometer(test_arr) == test_res


@pytest.mark.repeat(100)
def test_random():
    random_n = random.randint(1, 100)
    test_res = 0
    hours_prev = 0
    test_arr = []
    for _ in range(random_n):
        random_speed = random.randint(1, 100)
        test_arr.append(random_speed)
        random_hours = random.randint(hours_prev, 10)
        test_arr.append(random_hours)
        test_res += (random_hours - hours_prev) * random_speed
        hours_prev = random_hours

        if random_hours == 10:
            break

    assert odometer(test_arr) == test_res


def test_min_max():
    arr_min = [0, 0]
    arr_max = [10**20, 10**20]
    test_res_min = 0
    test_res_max = 10**20
    test_res_min = arr_min[0]
    test_res_max = arr_max[0] * arr_max[1]
    assert odometer(arr_min) == test_res_min
    assert odometer(arr_max) == test_res_max
