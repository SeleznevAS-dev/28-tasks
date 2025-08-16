def MadMax(N: int, Tele: list[int]) -> list[int]:
    Tele.sort()
    ans = Tele.copy()
    ans[N // 2], ans[-1] = ans[-1], ans[N // 2]
    start_pos = N // 2 + 1
    final_pos = (N // 2) + (N // 4) + 1
    countdown = 2
    for i in range(start_pos, final_pos):
        ans[i], ans[-countdown] = ans[-countdown], ans[i]
        countdown += 1
    return ans

