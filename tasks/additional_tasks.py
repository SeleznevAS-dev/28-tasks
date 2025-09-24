# 0.
def factorial(N: int) -> int:
    if N == 1:
        return 1
    return N * factorial(N - 1)


# 1.
def power(N: int, M: int) -> int:
    if M == 1:
        return N
    return N * power(N, M - 1)


# 2.
def sum_numbers(N: int) -> int:
    if len(str(N)) == 1:
        return N % 10
    return N % 10 + sum_numbers(N // 10)
