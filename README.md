# Multi-Algorithm Maze Visualizer

![Project Banner](https://via.placeholder.com/1200x400?text=Multi-Algorithm+Maze+Visualizer+Banner)
> *An interactive tool to visualize and compare pathfinding algorithms in real-time.*

## 📌 Overview

This project is a high-performance, interactive **Maze Visualizer** built with Python and Pygame. It allows users to generate complex mazes and watch how different Artificial Intelligence algorithms navigate through them to find the shortest path. 

The application provides a side-by-side comparison of four major pathfinding algorithms, tracking metrics like **Nodes Explored**, **Execution Time**, and **Path Length**.

---

## 🚀 Features

- **Real-time Visualization**: Watch the algorithms "think" as they explore the maze.
- **Dynamic Maze Generation**: Uses the **Recursive Backtracking** algorithm to create unique, solvable mazes every time.
- **Algorithm Comparison**: View BFS, DFS, Dijkstra, and A* simultaneously to compare their efficiency.
- **Interactive UI**: Resizable window support with real-time metric updates.
- **Cross-Platform**: Runs on Windows, macOS, and Linux.

---

## 📸 Visual Gallery

| Main Interface | Algorithm Comparison |
| :---: | :---: |
| ![Main Screen](https://via.placeholder.com/600x400?text=Main+Interface+Screenshot) | ![Comparison](https://via.placeholder.com/600x400?text=Algorithm+Comparison+Screenshot) |
| *Place an image of the initial screen here (R key)* | *Place an image of all algorithms running (SPACE key)* |

---

## 🛠️ Prerequisites & Installation

### 1. Requirements
- **Python 3.8+**: [Download here](https://www.python.org/downloads/)
- **Pygame**: The core engine for graphics and window management.

### 2. Setup Instructions

#### **For Windows**
1. Open Command Prompt or PowerShell.
2. Clone this repository or download the source code.
3. Navigate to the project folder:
   ```bash
   cd maze_ai_project
   ```
4. Install dependencies:
   ```bash
   pip install pygame
   ```
5. Run the application:
   ```bash
   python main.py
   ```

#### **For macOS / Linux**
1. Open the Terminal.
2. Install Pygame using pip:
   ```bash
   pip3 install pygame
   ```
3. Run the application:
   ```bash
   python3 main.py
   ```

---

## 🎮 How to Use

Once the application is running, use the following keyboard shortcuts to control the visualizer:

| Key | Action |
| :--- | :--- |
| **`R`** | **Reset**: Generate a brand new random maze. |
| **`SPACE`** | **Run All**: Start all 4 algorithms simultaneously. |
| **`B`** | **BFS**: Run Breadth-First Search only. |
| **`D`** | **DFS**: Run Depth-First Search only. |
| **`J`** | **Dijkstra**: Run Dijkstra’s Algorithm only. |
| **`A`** | **A*** | Run A* Search only. |
| **`ESC`** | **Exit**: Close the application. |

---

## 🧠 Deep Dive: The Algorithms

### 1. Breadth-First Search (BFS)
![BFS Visualization](https://via.placeholder.com/400x200?text=BFS+Exploration+Pattern)
- **Concept**: Explores neighbor nodes first, before moving to the next level neighbors.
- **Mechanism**: Uses a **Queue** (FIFO).
- **Pro**: Guaranteed to find the shortest path in an unweighted grid.
- **Con**: High memory usage as it explores in all directions equally.

### 2. Depth-First Search (DFS)
![DFS Visualization](https://via.placeholder.com/400x200?text=DFS+Exploration+Pattern)
- **Concept**: Goes as deep as possible along each branch before backtracking.
- **Mechanism**: Uses a **Stack** (LIFO).
- **Pro**: Low memory usage.
- **Con**: Does **not** guarantee the shortest path; often finds very long, winding routes.

### 3. Dijkstra's Algorithm
![Dijkstra Visualization](https://via.placeholder.com/400x200?text=Dijkstra+Exploration+Pattern)
- **Concept**: A classic greedy algorithm that finds the shortest path by tracking the minimum cost to reach each node.
- **Mechanism**: Uses a **Priority Queue**.
- **Note**: In this unweighted maze, it behaves similarly to BFS but is designed for weighted graphs.

### 4. A* Search (A-Star)
![A* Visualization](https://via.placeholder.com/400x200?text=A-Star+Exploration+Pattern)
- **Concept**: An "informed" search algorithm that uses heuristics to speed up the process.
- **Equation**: `f(n) = g(n) + h(n)`
  - `g(n)`: Actual cost from start to current node.
  - `h(n)`: Estimated cost from current node to goal (**Manhattan Distance**).
- **Pro**: Extremely efficient; finds the optimal path while exploring significantly fewer nodes than BFS/Dijkstra.

---

## 🏗️ Technical Architecture

### Maze Generation: Recursive Backtracking
The maze isn't just random noise; it's generated using a **Depth-First Search** approach for carving paths:
1. Start at a random cell.
2. Mark it as visited and choose a random unvisited neighbor.
3. Remove the wall between them and move to the neighbor.
4. If no neighbors are left, backtrack to the previous cell.
5. Repeat until all cells are visited.

### Project Structure
```text
maze_ai_project/
├── main.py              # Main Entry point & UI Logic
├── algorithms/          # Logic for all AI searches
│   ├── bfs.py           # Breadth-First Search
│   ├── dfs.py           # Depth-First Search
│   ├── dijkstra.py      # Dijkstra's Algorithm
│   └── astar.py         # A* Search with Manhattan Heuristic
└── README.md            # You are here!
```

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for new algorithms (like Greedy Best-First or Bidirectional Search) or UI improvements:
1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---
**Made with ❤️ for AI Enthusiasts**
