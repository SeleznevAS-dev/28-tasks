from tasks.task_3 import ConquestCampaign


def test_regression():
    test_N = 3
    test_M = 4
    test_L1 = 2
    test_battalion1 = [2, 2, 3, 4]
    test_L2 = 3
    test_battalion2 = [2, 2, 2, 2, 3, 4]
    test_res = 3
    assert ConquestCampaign(test_N, test_M, test_L1, test_battalion1) == test_res
    assert ConquestCampaign(test_N, test_M, test_L2, test_battalion2) == test_res
