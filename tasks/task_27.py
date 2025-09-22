def sort_arr(arr: list[int], n: int) -> list[int]:
    res = []
    for _ in range(n):
        mn = min(arr)
        res.append(mn)
        arr.remove(mn)
    return res


def Football(F: list[int], N: int) -> bool:
    arr_to_sort = F.copy()
    sorted_arr = sort_arr(arr_to_sort, N)
    wrong_positions = []
    for i in range(N):
        if F[i] != sorted_arr[i]:
            wrong_positions.append(i)
    can_sort = False
    if (len(wrong_positions) == 2) or (
        F[wrong_positions[0] : wrong_positions[-1] + 1][::-1]
        == sorted_arr[wrong_positions[0] : wrong_positions[-1] + 1]
    ):
        can_sort = True
    return can_sort
