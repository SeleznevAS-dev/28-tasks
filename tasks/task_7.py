def WordSearch(width: int, s: str, subs: str) -> list[int]:
    # Part 1
    strings = []
    free_space = width
    length = 0
    i_start = 0
    i_last = 0
    previous_string = ""
    s += " "
    length_s = len(s)
    for i in range(length_s):
        if s[i] == " ":
            if length <= free_space:
                if len(strings) != 0:
                    previous_string = (strings.pop()) + " "
                new_string = previous_string + "".join(s[i_start:i_last])
                strings.append(new_string)
                free_space -= i - i_start + 1
            else:
                if length <= width:
                    free_space = width
                    new_string = s[i_start:i_last]
                    strings.append(new_string)
                    free_space -= i - i_start + 1
                else:
                    cycles = length // width
                    for k in range(cycles + 1):
                        free_space = width
                        if k < cycles:
                            i_last = i_start + width
                        else:
                            i_last = i
                        new_string = "".join(s[i_start:i_last])
                        strings.append(new_string)
                        free_space -= i - i_last + 1
                        i_start = i_last
                        assert len(strings[-1]) <= width
            i_start = i + 1
            assert len(strings[-1]) <= width
            length = 0
        else:
            i_last = i + 1
            length += 1

    # Part 2
    ans = []
    for string in strings:
        for word in string.split(" "):
            if word == subs:
                ans.append(1)
                break
        else:
            ans.append(0)
    return ans
