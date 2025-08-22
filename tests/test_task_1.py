import math
import random
# import pytest
from tasks.task_1 import squirrel


def test_regression():
    random_n = random.randint(1, 100)
    res = math.factorial(random_n)
    test_res = int(str(res)[0])
    assert squirrel(random_n) == test_res


# def test_min_max():
#     n_min = 1
#     n_max = 10**3
#     res_min = math.factorial(n_min)
#     res_max = math.factorial(n_max)
#     test_res_min = int(str(res_min)[0])
#     test_res_max = int(str(res_max)[0])
#     assert squirrel(n_min) == test_res_min
#     assert squirrel(n_max) == test_res_max

# @pytest.mark.repeat(100)
# def test_random():
#     random_n = random.randint(1, 1000)
#     res = math.factorial(random_n)
#     test_res = int(str(res)[0])
#     assert squirrel(random_n) == test_res