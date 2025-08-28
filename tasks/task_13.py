def UFO(N: int, data: list[int], octal: bool) -> list[int]:
    number_system = 8 if octal else 16
    ans = []
    for i in range(N):
        sm = 0
        number = str(data[i])
        for index, element in enumerate(number[::-1]):
            sm += int(element) * number_system**index
        ans.append(sm)
    return ans
