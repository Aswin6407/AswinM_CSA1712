from collections import deque

def water_jug(capacity_a, capacity_b, target):
    queue = deque()
    visited = set()

    queue.append((0, 0, []))

    while queue:
        a, b, path = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        path = path + [(a, b)]

        if a == target or b == target:
            return path

        states = [
            (capacity_a, b),
            (a, capacity_b),
            (0, b),
            (a, 0)
        ]

        transfer = min(a, capacity_b - b)
        states.append((a - transfer, b + transfer))

        transfer = min(b, capacity_a - a)
        states.append((a + transfer, b - transfer))

        for state in states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    return None


capacity_a = 4
capacity_b = 3
target = 2

solution = water_jug(capacity_a, capacity_b, target)

if solution:
    print("Solution found!")
    print()

    for step, state in enumerate(solution):
        print("Step", step, ":", state[0], "litres,", state[1], "litres")
else:
    print("No solution found.")