def alpha_beta(depth, node, maximizing, values,
               alpha, beta, max_depth):
    if depth == max_depth:
        return values[node]

    if maximizing:
        best = float("-inf")

        for i in range(2):
            value = alpha_beta(
                depth + 1,
                node * 2 + i,
                False,
                values,
                alpha,
                beta,
                max_depth
            )

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                print("Branch pruned at node", node)
                break

        return best

    else:
        best = float("inf")

        for i in range(2):
            value = alpha_beta(
                depth + 1,
                node * 2 + i,
                True,
                values,
                alpha,
                beta,
                max_depth
            )

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                print("Branch pruned at node", node)
                break

        return best


leaf_values = [3, 5, 2, 9, 12, 5, 23, 23]

result = alpha_beta(
    0, 0, True, leaf_values,
    float("-inf"), float("inf"), 3
)

print("Leaf Values:", leaf_values)
print("Best Value using Alpha-Beta Pruning:", result)