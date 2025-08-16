from tasks.task_3 import ConquestCampaign


def test_regression():
    test_N = 3
    test_M = 4
    test_L = 2
    test_battalion = [2, 2, 3, 4]
    test_res = 3
    assert ConquestCampaign(test_N, test_M, test_L, test_battalion) == test_res

