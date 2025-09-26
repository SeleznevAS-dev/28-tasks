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


# 3.
def list_len(arr: list) -> int:
    if len(arr) == 1:
        return 1
    arr.pop()
    return 1 + list_len(arr)


# 4.
def is_palindrome(string: str) -> bool:
    if len(string) > 2 and not is_palindrome(string[1:-1]):
        return False

    ans = False
    if (string[0] == string[-1]) or len(string) == 1:
        ans = True
    elif string[0] != string[-1]:
        ans = False

    return ans
