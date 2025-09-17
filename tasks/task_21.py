def BiggerGreater(input: str) -> str:
    input_arr = list(input)
    input_arr_start = input_arr.copy()

    for i in range(len(input_arr) - 1, 0, -1):
        if input_arr[i] > input_arr[i - 1]:
            break

    mn = min(
        list(filter(lambda x: x >= input_arr[i - 1], input_arr[i : len(input_arr)]))
    )

    input_arr[input_arr.index(mn, i, len(input_arr))], input_arr[i - 1] = (
        input_arr[i - 1],
        input_arr[input_arr.index(mn, i, len(input_arr))],
    )

    input_arr[i : len(input_arr)] = sorted(input_arr[i : len(input_arr)])
    if input_arr == input_arr_start:
        return ""
    return "".join(input_arr)
