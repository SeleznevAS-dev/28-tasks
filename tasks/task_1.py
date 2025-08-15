def squirrel(N: int) -> int:
    num = 1
    for i in range(2, N + 1):
        num *= i
    ans = int(str(num)[0])
    return ans