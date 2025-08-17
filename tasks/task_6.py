def PatternUnlock(N: int, hits: list[int]) -> str:
    screen = [[4, 5, 6], [3, 2, 1], [7, 8, 9]]
    ans = 0
    for i in range(1, N):
        for j in range(len(screen)):
            if hits[i] in screen[j]:
                for k in range(3):
                    if hits[i - 1] in screen[k]:
                        if hits[i - 1] in screen[j] or (
                            screen[k].index(hits[i - 1]) == screen[j].index(hits[i])
                        ):
                            ans += 1
                        else:
                            ans += 2 ** (0.5)

    return str(round(ans, 5)).replace(".", "").replace("0", "")

