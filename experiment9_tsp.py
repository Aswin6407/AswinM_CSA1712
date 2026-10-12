from itertools import permutations

def tsp(graph, start):
    cities = list(graph.keys())
    cities.remove(start)

    min_cost = float('inf')
    best_path = None

    for route in permutations(cities):
        path = [start] + list(route) + [start]
        cost = 0

        for i in range(len(path) - 1):
            cost += graph[path[i]][path[i + 1]]

        if cost < min_cost:
            min_cost = cost
            best_path = path

    return best_path, min_cost


graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

path, cost = tsp(graph, 'A')

print("Best Route:", " -> ".join(path))
print("Minimum Cost:", cost)