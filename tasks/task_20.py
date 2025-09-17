s = ""
s_changes = []
pos = -1


def BastShoe(command: str) -> str:
    global s
    global s_changes
    global pos
    operation, argument = command[0], command[2:]
    if (
        (operation == "1" or operation == "2")
        and (pos < len(s_changes) - 1)
        and (pos != -1)
    ):
        s_changes = [s_changes[pos]]
        pos = 0
    if operation == "1":
        s += argument
        s_changes.append(s)
        pos += 1
    elif operation == "2" and int(argument) > len(s):
        s = ""
        s_changes.append(s)
        pos += 1
    elif operation == "2":
        s = s[0 : len(s) - int(argument)]
        s_changes.append(s)
        pos += 1
    elif operation == "3" and int(argument) > len(s) - 1:
        return ""
    elif operation == "3":
        return s[int(argument)]
    elif operation == "4" and pos == 0:
        s = s_changes[pos]
    elif operation == "4":
        pos -= 1
        s = s_changes[pos]
    elif operation == "5" and pos == len(s_changes) - 1:
        s = s_changes[pos]
    elif operation == "5":
        pos += 1
        s = s_changes[pos]
    return s
