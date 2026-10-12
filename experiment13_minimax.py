def minimax(depth, node, maximizing, values, max_depth):
    if depth == max_depth:
        return values[node]

    if maximizing:
        best = float("-inf")

        for i in range(2):
            value = minimax(
                depth + 1,
                node * 2 + i,
                False,
                values,
                max_depth
            )
            best = max(best, value)

        return best

    else:
        best = float("inf")

        for i in range(2):
            value = minimax(
                depth + 1,
                node * 2 + i,
                True,
                values,
                max_depth
            )
            best = min(best, value)

        return best


leaf_values = [3, 5, 2, 9, 12, 5, 23, 23]

result = minimax(0, 0, True, leaf_values, 3)

print("Leaf Values:", leaf_values)
print("Best Value using Minimax:", result)