def TankRush(H1: int, W1: int, S1: str, H2: int, W2: int, S2: str) -> bool:
    arr1 = []
    for i in S1.split(" "):
        arr1.append(i)
    arr2 = []
    for i in S2.split(" "):
        arr2.append(i)

    first_s2_line = arr2[0]
    for i in range(H1 - H2 + 1):
        line1 = arr1[i]

        for k in range(W1 - W2 + 1):
            indexes = []
            s_line1 = line1[k]
            for h in range(W2):
                s_line2 = first_s2_line[h]
                if s_line1 == s_line2 and indexes == []:
                    indexes.append(k)
                elif s_line1 == s_line2 and len(indexes) == 1 and h == W2 - 1:
                    indexes.append(k + h)
                    break
                elif s_line1 != s_line2:
                    break
                s_line1 = line1[k + h + 1]
            if len(indexes) == 2 and H2 == 1:
                return True

            elif len(indexes) == 2:
                seq = [i + 1, H1 - H2 + 2]
                for index, n in enumerate(seq, start=1):
                    line1_check = arr1[n]
                    line2_check = arr2[index]
                    if line1_check[indexes[0] : indexes[1] + 1] != line2_check:
                        break
                    elif (
                        line1_check[indexes[0] : indexes[1] + 1] == line2_check
                        and index == H2 - 1
                    ):
                        return True

    return False
