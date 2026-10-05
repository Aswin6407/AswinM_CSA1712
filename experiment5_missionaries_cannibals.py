from collections import deque

def is_valid(m_left, c_left, m_right, c_right):
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False

    if m_left > 0 and m_left < c_left:
        return False

    if m_right > 0 and m_right < c_right:
        return False

    return True


def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque()
    visited = set()

    queue.append((start, []))

    moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ]

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        m_left, c_left, boat = state
        m_right = 3 - m_left
        c_right = 3 - c_left

        if state == goal:
            return path

        for m, c in moves:
            if boat == 0:
                new_m_left = m_left - m
                new_c_left = c_left - c
                new_boat = 1
            else:
                new_m_left = m_left + m
                new_c_left = c_left + c
                new_boat = 0

            new_m_right = 3 - new_m_left
            new_c_right = 3 - new_c_left

            if is_valid(new_m_left, new_c_left, new_m_right, new_c_right):
                new_state = (new_m_left, new_c_left, new_boat)

                if new_state not in visited:
                    queue.append((new_state, path))

    return None


solution = solve()

if solution:
    print("Solution found!")
    print()

    for step, state in enumerate(solution):
        m_left, c_left, boat = state
        m_right = 3 - m_left
        c_right = 3 - c_left

        side = "Left" if boat == 0 else "Right"

        print(
            "Step", step,
            ": Left =", m_left, "Missionaries,", c_left, "Cannibals |",
            "Right =", m_right, "Missionaries,", c_right, "Cannibals |",
            "Boat =", side
        )
else:
    print("No solution found.")