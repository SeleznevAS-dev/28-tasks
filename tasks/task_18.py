def MisterRobot(N: int, data: list[int]) -> bool:
    data_sorted = sorted(data.copy())
    sort = -1  # -1 not sorted 1 can sort 0 can't sort
    i = 0
    j = 3
    while sort == -1:
        assert j <= len(data)
        n = 0
        while (data[i:j] != sorted(data[i:j])) and n < 3:
            data[i], data[i + 1], data[i + 2] = data[i + 1], data[i + 2], data[i]
            n += 1
        if n == 3:
            sort = 0
        elif data == data_sorted:
            sort = 1
        elif n == 0:
            i += 1
            j += 1
        else:
            i = 0
            j = 3

    return bool(sort)
