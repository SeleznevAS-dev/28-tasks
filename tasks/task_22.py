def SherlockValidString(s: str) -> bool:
    s_arr = sorted(list(s))
    counts = []
    i = 0
    while sum(counts) < len(s_arr):
        c = s_arr.count(s_arr[i])
        counts.append(c)
        i += c
    mn = min(counts)
    mx = max(counts)
    if mn == mx:
        return True
    elif (mx - mn == 1) and counts.count(mx) == 1:
        return True
    elif (mx - mn == 1) and counts.count(mn) == 1:
        return True
    return False
