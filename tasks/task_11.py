def BigMinus(s1: str, s2: str) -> str:
    need_to_swap = True
    if len(s1) > len(s2):
        need_to_swap = False
    elif len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] < s2[i]:
                break
            elif s1[i] > s2[i]:
                need_to_swap = False
                break
    if need_to_swap:
        s1, s2 = s2, s1
    len1 = len(s1)
    len2 = len(s2)
    s1 = list(s1)
    s2 = list(s2)
    ans = []
    need_to_decrease = False
    for i in range(-1, -len1 - 1, -1):
        diff = 0
        num1 = int(s1[i])
        if need_to_decrease and num1 == 0:
            num1 = 9
            need_to_decrease = True
        elif need_to_decrease:
            num1 -= 1
            need_to_decrease = False
        if -(i + 1) <= len2 - 1:
            num2 = int(s2[i])
            diff = num1 - num2
            if diff < 0:
                diff = 10 - abs(diff)
                need_to_decrease = True
        else:
            diff = num1

        ans.append(abs(diff))

    ans.reverse()
    if need_to_decrease and ans[0] != 0:
        ans[0] -= 1
    ans = map(str, ans)
    ans = "".join(ans).lstrip("0")
    return ans or "0"
