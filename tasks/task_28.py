def Keymaker(k: int) -> str:
    doors = []
    for _ in range(k):
        doors.append(1)
    for i in range(2, k + 1):
        for j in range(i - 1, k, i):
            doors[j] = 0 if doors[j] == 1 else 1
    return "".join(map(str, doors))
