def odometer(oksana: list[int]) -> int:
    n = len(oksana)
    ans = 0
    for i in range(0, n, 2):
        ans += oksana[i]
    return ans

