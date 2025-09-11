def add_to_ans(ans: list, arr: list, value: int) -> list:
    arr.sort()
    for i in arr:
        ans.append(f"{i} {value}")
    arr = []
    return ans, arr


def ShopOLAP(N: int, items: list[str]) -> list[str]:
    items_dict = {}
    nums = []
    for i in range(N):
        item = items[i]
        name, count = item.split(" ")
        if name in items_dict.keys():
            items_dict[name] += int(count)
        else:
            items_dict[name] = int(count)
    items_dict_sorted = dict(
        sorted(items_dict.items(), reverse=True, key=lambda items: items[1])
    )
    for num in items_dict_sorted.values():
        nums.append(num)
    ans = []
    arr = []
    for key, value in items_dict_sorted.items():
        if nums.count(value) > 1 and len(arr) == nums.count(value) - 1:
            arr.append(key)
            ans, arr = add_to_ans(ans, arr, value)
        elif nums.count(value) > 1:
            arr.append(key)
        else:
            ans.append(f"{key} {value}")
    return ans
