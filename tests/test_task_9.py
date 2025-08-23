from tasks.task_9 import TheRabbitsFoot


def test_regression():
    test_s = "отдай мою кроличью лапку"
    test_encode = True
    assert TheRabbitsFoot(test_s, test_encode) == "омоюу толл дюиа акчп йрьк"


def test_regression2():
    test_s = "омоюу толл дюиа акчп йрьк"
    test_encode = False
    assert TheRabbitsFoot(test_s, test_encode) == "отдаймоюкроличьюлапку"
