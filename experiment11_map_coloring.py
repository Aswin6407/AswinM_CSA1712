colors = ["Red", "Green", "Blue"]

map_graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

assignment = {}


def is_safe(region, color):
    for neighbor in map_graph[region]:
        if assignment.get(neighbor) == color:
            return False
    return True


def solve(regions):
    if not regions:
        return True

    region = regions[0]

    for color in colors:
        if is_safe(region, color):
            assignment[region] = color

            if solve(regions[1:]):
                return True

            del assignment[region]

    return False


if solve(list(map_graph.keys())):
    print("Map Coloring Solution:")
    for region, color in assignment.items():
        print(region, ":", color)
else:
    print("No solution exists.")