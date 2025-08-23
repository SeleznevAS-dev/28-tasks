def TheRabbitsFoot(s: str, encode: bool) -> str:
    matrix = []
    ans = ""
    if not encode:
        words = s.split(" ")
        for word in words:
            arr = []
            for i in word:
                arr.append(i)
            matrix.append(arr)

        while matrix[0] != []:
            for j in range(len(matrix)):
                if matrix[j] != []:
                    ans += matrix[j].pop(0)
        return ans
    else:
        s = s.replace(" ", "")
        list_s = list(s)
        s_len = len(s)
        size = str(s_len**0.5).replace(".", "")
        rows = int(size[0])
        columns = int(size[1])
        while rows * columns < s_len:
            rows += 1
        for _ in range(rows):
            arr = []
            n = 0
            while len(list_s) > 0 and n < columns:
                arr.append(list_s.pop(0))
                n += 1
            matrix.append(arr)
        matrix_len = len(matrix)
        while len(matrix[0]) != 0:
            for i in range(matrix_len):
                if len(matrix[i]) != 0:
                    ans += matrix[i].pop(0)
            ans += " "
            matrix_len = len(matrix)
        return ans.rstrip()

