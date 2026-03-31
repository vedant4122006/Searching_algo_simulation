import time
import heapq

def heuristic(a, b):
    """
    Heuristic function (Manhattan Distance)
    Used to estimate distance to goal.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, rows):
    """
    A* Algorithm
    Combines:
    - Dijkstra (actual cost)
    - Heuristic (estimated cost)
    
    f(n) = g(n) + h(n)
    """

    start = None
    goal = None

    # Find start and goal
    for r in range(rows):
        for c in range(rows):
            if grid[r][c] == "S":
                start = (r, c)
            elif grid[r][c] == "G":
                goal = (r, c)

    # Priority Queue → (f_score, node)
    pq = []
    heapq.heappush(pq, (0, start))

    # g(n) → cost from start
    g_cost = {start: 0}

    # parent tracking
    parent = {}

    nodes_visited = 0
    start_time = time.time()

    while pq:
        _, current = heapq.heappop(pq)
        nodes_visited += 1

        yield ("visit", current, nodes_visited)

        if current == goal:
            break

        r, c = current
        neighbors = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]

        for nr, nc in neighbors:
            if 0 <= nr < rows and 0 <= nc < rows:
                if grid[nr][nc] != 1:
                    new_cost = g_cost[current] + 1

                    if (nr, nc) not in g_cost or new_cost < g_cost[(nr, nc)]:
                        g_cost[(nr, nc)] = new_cost

                        # f(n) = g(n) + h(n)
                        f_score = new_cost + heuristic((nr, nc), goal)

                        heapq.heappush(pq, (f_score, (nr, nc)))
                        parent[(nr, nc)] = current

    # -----------------------------
    # PATH RECONSTRUCTION
    # -----------------------------
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