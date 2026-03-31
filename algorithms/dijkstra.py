import time
import heapq  # Priority Queue (important for Dijkstra)

def dijkstra(grid, rows):
    """
    Dijkstra's Algorithm
    Finds the shortest path in a weighted graph.
    
    In our case:
    - All moves cost 1 → behaves similar to BFS
    - But uses priority queue (more advanced concept)
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

    # Priority Queue → (cost, node)
    pq = []
    heapq.heappush(pq, (0, start))

    # Distance from start to each node
    dist = {start: 0}

    # To reconstruct path later
    parent = {}

    nodes_visited = 0
    start_time = time.time()

    while pq:
        cost, current = heapq.heappop(pq)
        nodes_visited += 1

        # Show animation step
        yield ("visit", current, nodes_visited)

        if current == goal:
            break

        r, c = current
        neighbors = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]

        for nr, nc in neighbors:
            if 0 <= nr < rows and 0 <= nc < rows:
                if grid[nr][nc] != 1:
                    new_cost = cost + 1  # all edges weight = 1

                    # If new path is shorter → update
                    if (nr, nc) not in dist or new_cost < dist[(nr, nc)]:
                        dist[(nr, nc)] = new_cost
                        heapq.heappush(pq, (new_cost, (nr, nc)))
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