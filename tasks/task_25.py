def Transform(A: list[int], N: int) -> list:
    B = []
    for i in range(N):
        for j in range(N - i):
            k = i + j
            if A[j : k + 1] != []:
                B.append(max(A[j : k + 1]))
    return B


def TransformTransform(A: list[int], N: int) -> bool:
    B = Transform(A, N)
    return bool(sum(Transform(B, len(B))) % 2 == 0)
