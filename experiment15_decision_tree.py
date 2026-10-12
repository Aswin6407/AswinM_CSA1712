from math import log2
from collections import Counter


data = [
    (["Sunny", "Hot"], "No"),
    (["Sunny", "Mild"], "No"),
    (["Rainy", "Hot"], "Yes"),
    (["Rainy", "Mild"], "Yes"),
    (["Cloudy", "Hot"], "Yes"),
    (["Cloudy", "Mild"], "Yes")
]

features = ["Weather", "Temperature"]


def entropy(labels):
    total = len(labels)
    counts = Counter(labels)

    return -sum(
        (count / total) * log2(count / total)
        for count in counts.values()
    )


def information_gain(data, feature_index):
    total_entropy = entropy([row[1] for row in data])
    values = set(row[0][feature_index] for row in data)

    weighted_entropy = 0

    for value in values:
        subset = [row for row in data
                  if row[0][feature_index] == value]

        weighted_entropy += (
            len(subset) / len(data)
        ) * entropy([row[1] for row in subset])

    return total_entropy - weighted_entropy


def build_tree(data, available_features):
    labels = [row[1] for row in data]

    if len(set(labels)) == 1:
        return labels[0]

    if not available_features:
        return Counter(labels).most_common(1)[0][0]

    best_feature = max(
        available_features,
        key=lambda index: information_gain(data, index)
    )

    tree = {features[best_feature]: {}}

    for value in set(row[0][best_feature] for row in data):
        subset = [row for row in data
                  if row[0][best_feature] == value]

        remaining = [
            index for index in available_features
            if index != best_feature
        ]

        tree[features[best_feature]][value] = build_tree(
            subset, remaining
        )

    return tree


tree = build_tree(data, list(range(len(features))))

print("Decision Tree:")
print(tree)