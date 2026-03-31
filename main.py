import pygame
import sys
import random
import os

# Import the search algorithms from separate files.
# This keeps the project organized and easier to explain.
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.dijkstra import dijkstra
from algorithms.astar import astar

# -----------------------------
# BASIC WINDOW SETUP
# -----------------------------
# This centers the window when it opens.
os.environ["SDL_VIDEO_CENTERED"] = "1"

# Start pygame.
pygame.init()

# Read the user's screen size so the app can scale nicely.
display_info = pygame.display.Info()

# Create a window that is 85% of the screen size.
# This keeps the app big enough for exhibition, but still resizable.
WIDTH = int(display_info.current_w * 0.85)
HEIGHT = int(display_info.current_h * 0.85)

# Create a normal resizable window.
# This gives minimize, maximize, and close buttons.
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Multi-Algorithm Maze Visualizer")

# -----------------------------
# MAZE SETTINGS
# -----------------------------
# We use an odd number because the maze carving method works better with it.
ROWS = 31

# Start and goal positions in the grid.
# Start is near the top-left.
# Goal is near the bottom-right.
start = (1, 1)
goal = (ROWS - 2, ROWS - 2)

# -----------------------------
# COLORS
# -----------------------------
# White background.
WHITE = (255, 255, 255)

# Maze wall color.
BLACK = (30, 30, 30)

# Start node color.
GREEN = (46, 204, 113)

# Goal node color.
RED = (231, 76, 60)

# Text and UI color.
BLUE = (52, 152, 219)

# Final shortest path color.
PATH = (241, 196, 15)

# Different visited colors for each algorithm.
V_BFS = (173, 216, 230)
V_DFS = (255, 182, 193)
V_DIJ = (144, 238, 144)
V_AST = (221, 160, 221)

# -----------------------------
# FONTS
# -----------------------------
# Title font for algorithm names.
font_title = pygame.font.SysFont("arial", 24, bold=True)

# Small font for metrics and instructions.
font_small = pygame.font.SysFont("arial", 16)

# -----------------------------
# MAZE DATA
# -----------------------------
# This 2D list stores the maze.
# 1 = wall
# 0 = open cell
# "S" = start
# "G" = goal
grid = []

# -----------------------------
# ALGORITHM STATE
# -----------------------------
# Every algorithm has its own state:
# - gen: the generator object
# - visited: explored cells
# - path: final path
# - metrics: nodes/time
# - color: visited-cell color
states = {
    "BFS": {
        "gen": None,
        "visited": set(),
        "path": [],
        "metrics": {"nodes": 0, "time": 0},
        "color": V_BFS,
    },
    "DFS": {
        "gen": None,
        "visited": set(),
        "path": [],
        "metrics": {"nodes": 0, "time": 0},
        "color": V_DFS,
    },
    "Dijkstra": {
        "gen": None,
        "visited": set(),
        "path": [],
        "metrics": {"nodes": 0, "time": 0},
        "color": V_DIJ,
    },
    "A*": {
        "gen": None,
        "visited": set(),
        "path": [],
        "metrics": {"nodes": 0, "time": 0},
        "color": V_AST,
    },
}

# Match algorithm names to their import functions.
algorithm_functions = {
    "BFS": bfs,
    "DFS": dfs,
    "Dijkstra": dijkstra,
    "A*": astar,
}

# -----------------------------
# MAZE GENERATION
# -----------------------------
def reset_algorithms():
    """
    Clear all algorithm animation data.
    This is used when we generate a new maze.
    """
    for algo_name in states:
        states[algo_name]["gen"] = None
        states[algo_name]["visited"].clear()
        states[algo_name]["path"].clear()
        states[algo_name]["metrics"] = {"nodes": 0, "time": 0}


def generate_maze():
    """
    Generate a proper maze using recursive backtracking.
    This makes a corridor-style maze, not random noise.
    The maze is guaranteed to be connected.
    """
    global grid

    # Start with every cell blocked as a wall.
    grid = [[1 for _ in range(ROWS)] for _ in range(ROWS)]

    def carve(x, y):
        """
        Recursive maze carving function.
        It moves in steps of 2 so walls remain between paths.
        """
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Stay inside the border.
            if 0 < nx < ROWS - 1 and 0 < ny < ROWS - 1:
                # If the destination has not been carved yet, open it.
                if grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    # Open the wall between current cell and destination.
                    grid[x + dx // 2][y + dy // 2] = 0
                    carve(nx, ny)

    # Start carving from the start cell.
    grid[start[0]][start[1]] = 0
    carve(start[0], start[1])

    # Mark start and goal.
    grid[start[0]][start[1]] = "S"
    grid[goal[0]][goal[1]] = "G"

    # When a new maze is created, all previous algorithm results are cleared.
    reset_algorithms()


# -----------------------------
# DRAWING HELPERS
# -----------------------------
def draw_text(text, x, y, font, color=BLUE):
    """
    Draw text on the screen.
    """
    label = font.render(text, True, color)
    screen.blit(label, (x, y))


def start_algorithm(name):
    """
    Start one algorithm by creating its generator.
    The algorithm will run step by step on each frame.
    """
    states[name]["gen"] = algorithm_functions[name](grid, ROWS)
    states[name]["visited"].clear()
    states[name]["path"].clear()
    states[name]["metrics"] = {"nodes": 0, "time": 0}


def reset_all_running_algorithms():
    """
    Stop all running algorithms and clear their visual data.
    """
    for name in states:
        states[name]["gen"] = None
        states[name]["visited"].clear()
        states[name]["path"].clear()
        states[name]["metrics"] = {"nodes": 0, "time": 0}


def draw_panel(panel_x, panel_y, panel_w, panel_h, name):
    """
    Draw one quadrant of the screen.

    Each panel has:
    - algorithm title at the top
    - maze on the left
    - metrics on the right
    """
    data = states[name]

    # Basic spacing values.
    padding = 10
    title_h = 30
    metrics_w = 150

    # Draw the algorithm name.
    draw_text(name, panel_x + padding, panel_y, font_title, BLUE)

    # The maze starts below the title.
    maze_x = panel_x + padding
    maze_y = panel_y + title_h

    # Space available for the maze inside the panel.
    maze_available_w = panel_w - metrics_w - (padding * 3)
    maze_available_h = panel_h - title_h - (padding * 2)

    # Make the maze area square.
    maze_size = min(maze_available_w, maze_available_h)

    # Each cell size is based on the available square area.
    cell_size = max(1, maze_size // ROWS)

    # Real maze size after rounding cell size.
    maze_render_size = cell_size * ROWS

    # Draw the maze cells.
    for r in range(ROWS):
        for c in range(ROWS):
            value = grid[r][c]
            pos = (r, c)

            # Default color for this cell.
            color = WHITE

            # If this algorithm has already found a path, draw the path first.
            if pos in data["path"]:
                color = PATH

            # If this cell was visited by the algorithm, draw visited color.
            elif pos in data["visited"]:
                color = data["color"]

            # Otherwise draw the maze structure itself.
            elif value == 1:
                color = BLACK
            elif value == "S":
                color = GREEN
            elif value == "G":
                color = RED

            # Draw the cell.
            pygame.draw.rect(
                screen,
                color,
                (
                    maze_x + c * cell_size,
                    maze_y + r * cell_size,
                    cell_size,
                    cell_size,
                ),
            )

    # Metrics go on the right side of the same panel.
    metrics_x = maze_x + maze_render_size + 15
    metrics_y = maze_y + 10

    draw_text("Metrics", metrics_x, metrics_y, font_small, BLACK)
    draw_text(f"Nodes: {data['metrics']['nodes']}", metrics_x, metrics_y + 25, font_small, BLACK)
    draw_text(f"Time: {data['metrics']['time']}s", metrics_x, metrics_y + 45, font_small, BLACK)
    draw_text(f"Path: {len(data['path'])}", metrics_x, metrics_y + 65, font_small, BLACK)


def draw_header():
    """
    Draw the instruction line at the top.
    """
    draw_text(
        "R = New Maze | SPACE = Run All | B = BFS | D = DFS | J = Dijkstra | A = A* | ESC = Exit",
        20,
        10,
        font_small,
        BLUE,
    )


# -----------------------------
# MAIN LOOP
# -----------------------------
def main():
    global WIDTH, HEIGHT, screen

    clock = pygame.time.Clock()

    # Build the first maze when the app starts.
    generate_maze()

    running = True
    while running:
        # -------------------------
        # EVENT HANDLING
        # -------------------------
        for event in pygame.event.get():
            # Close button on the window.
            if event.type == pygame.QUIT:
                running = False

            # If the user resizes the window, update WIDTH and HEIGHT.
            if event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

            # Keyboard controls.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                # Regenerate the maze and stop everything.
                if event.key == pygame.K_r:
                    generate_maze()
                    reset_all_running_algorithms()

                # Run all algorithms together.
                if event.key == pygame.K_SPACE:
                    start_algorithm("BFS")
                    start_algorithm("DFS")
                    start_algorithm("Dijkstra")
                    start_algorithm("A*")

                # Run one algorithm only.
                if event.key == pygame.K_b:
                    start_algorithm("BFS")

                if event.key == pygame.K_d:
                    start_algorithm("DFS")

                # J is used for Dijkstra because D is already used by DFS.
                if event.key == pygame.K_j:
                    start_algorithm("Dijkstra")

                if event.key == pygame.K_a:
                    start_algorithm("A*")

        # -------------------------
        # STEP EACH RUNNING ALGORITHM
        # -------------------------
        # Each algorithm is a generator.
        # We advance it one step per frame so the search can be animated.
        for name, data in states.items():
            if data["gen"] is not None:
                try:
                    result = next(data["gen"])

                    # The generator says: "I visited one node".
                    if result[0] == "visit":
                        _, node, count = result
                        data["visited"].add(node)
                        data["metrics"]["nodes"] = count

                    # The generator says: "I am done".
                    elif result[0] == "done":
                        _, path, nodes, elapsed = result
                        data["path"] = path
                        data["metrics"]["nodes"] = nodes
                        data["metrics"]["time"] = elapsed
                        data["gen"] = None

                except StopIteration:
                    data["gen"] = None

        # -------------------------
        # DRAW EVERYTHING
        # -------------------------
        screen.fill(WHITE)

        # Header line at the top.
        draw_header()

        # Layout math.
        top_margin = 45
        gap = 20

        # Two columns and two rows.
        panel_w = (WIDTH - 3 * gap) // 2
        panel_h = (HEIGHT - top_margin - 3 * gap) // 2

        x1 = gap
        x2 = gap * 2 + panel_w
        y1 = top_margin
        y2 = top_margin + panel_h + gap

        # Four panels.
        draw_panel(x1, y1, panel_w, panel_h, "BFS")
        draw_panel(x2, y1, panel_w, panel_h, "DFS")
        draw_panel(x1, y2, panel_w, panel_h, "Dijkstra")
        draw_panel(x2, y2, panel_w, panel_h, "A*")

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()