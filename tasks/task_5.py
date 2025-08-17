def SynchronizingTables(N: int, ids: list[int], salary: list[int]) -> list[int]:
    salary.sort()
    ids_copy = ids.copy()
    ans = [0] * N
    for _ in range(N):
        min_num = min(ids_copy)
        index = ids.index(min_num)
        ans[index] = salary.pop(0)
        ids_copy.remove(min_num)

    return ans

