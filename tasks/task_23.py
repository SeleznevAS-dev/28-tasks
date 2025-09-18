def TreeOfLife(H: int, W: int, N: int, tree: list[str]) -> list[str]:
    new_tree = []
    for i in range(H):
        new_tree.append([])
        for j in range(W):
            new_tree[i].append(int(tree[i][j].replace(".", "0").replace("+", "1")))

    for n in range(N):
        leafs_to_delete = []
        for i in range(H):
            for j in range(W):
                new_tree[i][j] += 1
                if new_tree[i][j] >= 3 and (n % 2) == 1:
                    leafs_to_delete.append([i, j + 1])
                    leafs_to_delete.append([i, j - 1])
                    leafs_to_delete.append([i + 1, j])
                    leafs_to_delete.append([i - 1, j])
                    leafs_to_delete.append([i, j])

        for leaf in leafs_to_delete:
            h = leaf[0]
            w = leaf[1]
            if (h in [i for i in range(H)]) and (w in [i for i in range(W)]):
                new_tree[h][w] = 0

    for i in range(H):
        for j in range(W):
            new_tree[i][j] = "." if new_tree[i][j] == 0 else "+"
        new_tree[i] = "".join(new_tree[i])

    return new_tree
