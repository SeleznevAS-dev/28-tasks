def MatrixTurn(Matrix: list[str], M: int, N: int, T: int):
    for _ in range(T):
        new_matrix = []
        for i in range(M):
            new_matrix.append([])
            for j in range(N):
                new_matrix[i].append("")

        for i in range(M):
            for j in range(N):
                if i < M // 2 and j < (N - 1 - i) and j >= i:
                    new_matrix[i][j + 1] = Matrix[i][j]

                elif (i > M // 2 - 1) and (j < N - (M - i) + 1) and j >= M - i:
                    new_matrix[i][j - 1] = Matrix[i][j]

                elif i < M - 1 and ((j == N - 1) or (j == N - i - 1)):
                    new_matrix[i + 1][j] = Matrix[i][j]

                elif i > 0 and ((j == 0) or (j == M - i - 1)):
                    new_matrix[i - 1][j] = Matrix[i][j]

        for i in range(M):
            Matrix[i] = "".join(new_matrix[i])
