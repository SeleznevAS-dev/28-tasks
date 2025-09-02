def Unmanned(L: int, N: int, track: list[list[int]]) -> int:
    distance = 0
    states = []  # 0 - red, 1 - green
    lights_passed = 0
    for i in range(N):
        states.append(
            [0, track[i][1], track[i][2]]
        )  # current cycle, rest of cycle red, rest of cycle green,
    i = 0
    while True:
        if lights_passed == len(track):
            break
        for j in range(N):
            if states[j][0] == 0 and states[j][1] == 0:
                states[j][0] = 1
                states[j][1] = track[j][1] - 1
            elif states[j][0] == 0:
                states[j][1] -= 1
            elif states[j][0] == 1 and states[j][2] == 0:
                states[j][0] = 0
                states[j][2] = track[j][2] - 1
            elif states[j][0] == 1:
                states[j][2] -= 1
        if distance == track[lights_passed][0] and states[lights_passed][0] == 1:
            lights_passed += 1
            distance += 1
        elif distance < track[lights_passed][0]:
            distance += 1
        i += 1

    while distance < L:
        i += 1
        distance += 1
    return i
