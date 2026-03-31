import time

def dfs(grid, rows):
    start = None
    goal = None

    # Find start and goal
    for r in range(rows):
        for c in range(rows):
            if grid[r][c] == "S":
                start = (r, c)
            elif grid[r][c] == "G":
                goal = (r, c)

    stack = [start]  # LIFO structure
    visited = set([start])
    parent = {}

    nodes_visited = 0
    start_time = time.time()

    while stack:
        current = stack.pop()
        nodes_visited += 1

        yield ("visit", current, nodes_visited)

        if current == goal:
            break

        r, c = current
        neighbors = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]

        for nr, nc in neighbors:
            if 0 <= nr < rows and 0 <= nc < rows:
                if grid[nr][nc] != 1 and (nr, nc) not in visited:
                    stack.append((nr, nc))   # stack instead of queue
                    visited.add((nr, nc))
                    parent[(nr, nc)] = current

    # Reconstruct path
    path = []
    cur = goal

    while cur != start:
        path.append(cur)
        cur = parent.get(cur)
        if cur is None:
            break

    path.append(start)
    path.reverse()

    end_time = time.time()

    yield ("done", path, nodes_visited, round(end_time - start_time, 4))