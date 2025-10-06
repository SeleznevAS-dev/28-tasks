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
def print_only_odd_nums_recursive(arr: list[int], N: int) -> None:
    if N >= len(arr):
        return

    num = arr[N]
    if num % 2 == 0:
        print(num)

    return print_only_odd_nums_recursive(arr, N + 1)


def print_only_odd_nums(arr: list[int]) -> None:
    return print_only_odd_nums_recursive(arr, 0)


# 6.
def print_only_odd_indexes_recursive(arr: list[int], N: int) -> None:
    if N >= len(arr):
        return

    print(arr[N])

    return print_only_odd_indexes_recursive(arr, N + 2)


def print_only_odd_indexes(arr: list[int]) -> None:
    return print_only_odd_indexes_recursive(arr, 0)


# 7.
def find_second_max_recursive(
    arr: list[int], i: int, max1: int = None, max2: int = None
) -> int:
    if arr[i] > max1:
        max2 = max1
        max1 = arr[i]
    elif arr[i] > max2:
        max2 = arr[i]

    if i == len(arr) - 1:
        return max2

    return find_second_max_recursive(arr, i + 1, max1, max2)


def find_second_max(arr: list[int]) -> int:
    return find_second_max_recursive(arr, 0, min(arr), min(arr))


print(find_second_max([21, 2, 3]))
