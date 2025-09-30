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
def check_is_palindrome_recursive(string: str, N: int) -> bool:
    if N == 1 or (string[N - 1] == string[-N] and N < 3):
        return True
    elif string[N - 1] != string[-N]:
        return False

    return check_is_palindrome_recursive(string, N - 2)


def is_palindrome(string: str) -> bool:
    return check_is_palindrome_recursive(string, len(string))


# 5.
def print_only_odd_nums(arr: list[int]) -> None:
    num = arr.pop()
    if num % 2 == 0:
        print(num)
    if arr == []:
        return

    return print_only_odd_nums(arr)


# 6.
def print_only_odd_indexes(arr: list[int]) -> None:
    if len(arr) % 2 == 0:
        arr.pop()

    print(arr.pop())
    if arr == []:
        return
    arr.pop()

    return print_only_odd_indexes(arr)
