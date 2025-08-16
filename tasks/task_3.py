def ConquestCampaign(N: int, M: int, L: int, battalion: list[int]) -> int:
    field = []
    cords = 0
    for i in range(N):
        field.append([])
        for j in range(M):
            if battalion[cords] - 1 == i and battalion[cords + 1] - 1 == j:
                field[i].append(1)
                cords += 2
            else:
                field[i].append(0)
    ans = 1
    while True:
        done = 0
        cords_to_add = []
        for i in range(N):
            if 0 not in field[i]:
                done += 1
            if done == len(field):
                return ans
            for j in range(M):
                if field[i][j] == 1:
                    cords_to_add.append([i + 1, j])
                    cords_to_add.append([i - 1, j])
                    cords_to_add.append([i, j + 1])
                    cords_to_add.append([i, j - 1])
        for k in cords_to_add:
            if k[0] > (N - 1) or k[0] < 0 or k[1] > (M - 1) or k[1] < 0:
                continue
            field[k[0]][k[1]] = 1
        ans += 1

