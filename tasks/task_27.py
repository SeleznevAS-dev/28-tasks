def check_is_valid(F: list[int], N: int) -> list[int]:
    wrong_positions = []
    for i in range(N - 1):
        if F[i] > F[i + 1] and i not in wrong_positions:
            wrong_positions.append(i)
            wrong_positions.append(i + 1)
    return wrong_positions


def Football(F: list[int], N: int) -> bool:
    arr = check_is_valid(F, N)
    can_make_valid = False
    if len(arr) == 2:
        can_make_valid = True
    elif len(check_is_valid(F[arr[0] : arr[-1] + 1][::-1], len(arr))) == 0:
        can_make_valid = True

    return can_make_valid
