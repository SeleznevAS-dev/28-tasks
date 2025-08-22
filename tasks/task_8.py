def SumOfThe(N: int, data: list[int]) -> int:
    for i in range(N):
        potential_sums = data.copy()
        potential_sum = potential_sums.pop(i)
        sm = 0
        for j in range(N - 1):
            sm += potential_sums[j]
        if sm == potential_sum:
            return sm
    return 0

