def odometer(oksana: list[int]) -> int:
    hours = 0
    speed = oksana[0]
    n = len(oksana)
    ans = 0
    for i in range(1, n):
        if i % 2 == 1:
            ans += (oksana[i] - hours) * speed
            hours = oksana[i]
        else:
            speed = oksana[i]
    return ans

