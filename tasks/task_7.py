def WordSearch(width: int, s: str, subs: str) -> list[int]:
    # Part 1
    strings = []
    length_s = len(s)
    free_space = width
    i_start = 0
    i_end = 0
    i_old = 0
    length = 0
    previous_string = ""
    for i in range(length_s):
        if s[i] == " " or i == length_s - 1:
            if length <= free_space:
                i_end = i
                if len(strings) != 0:
                    previous_string = strings.pop()
                new_string = previous_string + "".join(s[i_old:i_end])
                strings.append(new_string)
                free_space -= i_end - i_old
            else:
                if length > width:
                    for k in range((length // width) + 1):
                        i_start = i_old + 1
                        if k != (length // width):
                            i_start = i_old + 1
                            i_end = i_old + width
                        else:
                            i_end = i
                        new_string = "".join(s[i_start:i_end])
                        strings.append(new_string)
                        free_space = width
                        free_space -= i - i_old + 1
                        i_old = i_end
                else:
                    free_space = width
                    free_space -= i - i_old
                    i_start = i_old + 1
                    i_end = i if i < length_s - 1 else i + 1
                    new_string = s[i_old + 1 : i_end]
                    strings.append(new_string)
            i_old = i
            length = 0
        else:
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
