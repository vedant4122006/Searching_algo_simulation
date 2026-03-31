# Multi-Algorithm Maze Visualizer

> *An interactive tool to visualize and compare pathfinding algorithms in real-time.*

## 📌 Overview

This project is a high-performance, interactive **Maze Visualizer** built with Python and Pygame. It allows users to generate complex mazes and watch how different Artificial Intelligence algorithms navigate through them to find the shortest path. 

![Main Interface](./Screenshot%202026-03-31%20164224.png)
*Full-screen visualization showing BFS, DFS, Dijkstra, and A\* running simultaneously.*

---

## 🚀 Features

- **Real-time Visualization**: Watch the algorithms "think" as they explore the maze.
- **Dynamic Maze Generation**: Uses the **Recursive Backtracking** algorithm to create unique, solvable mazes every time.
- **Algorithm Comparison**: View BFS, DFS, Dijkstra, and A* simultaneously to compare their efficiency.
- **Metric Tracking**: Real-time stats for Nodes Explored, Time Elapsed, and Path Length.

---

## 📊 Algorithm Comparison & Metrics

Below is a side-by-side comparison of how each algorithm approaches the same maze. Each search pattern is unique to the logic of the underlying algorithm.

| BFS (Breadth-First) | DFS (Depth-First) |
| :---: | :---: |
| ![BFS](./Screenshot%202026-03-31%20164429.png) | ![DFS](./Screenshot%202026-03-31%20164454.png) |
| **Exploration**: Wide & Radial | **Exploration**: Deep & Linear |

| Dijkstra's Algorithm | A* Search (A-Star) |
| :---: | :---: |
| ![Dijkstra](./Screenshot%202026-03-31%20164439.png) | ![A*](./Screenshot%202026-03-31%20164505.png) |
| **Exploration**: Uniform Expansion | **Exploration**: Targeted/Directional |

### Performance Analysis

1. **Nodes Explored (Efficiency)**:
   - **A*** is the most efficient, as it uses a heuristic (Manhattan Distance) to "aim" toward the goal, resulting in the lowest node count.
   - **BFS** and **Dijkstra** explore a high number of nodes because they search in every possible direction until the goal is found.
   - **DFS** explores nodes randomly and often visits unnecessary branches.

2. **Time Elapsed**:
   - **A*** typically finishes first due to its targeted nature.
   - **BFS/Dijkstra** take longer as they must "fill" the maze areas.

3. **Path Length (Optimality)**:
   - **BFS, Dijkstra, and A*** are guaranteed to find the **Shortest Path** in this grid.
   - **DFS** often finds a significantly longer, non-optimal path because it doesn't prioritize distance.

---

## 🛠️ Installation & Setup

### 1. Requirements
- **Python 3.8+**
- **Pygame**

### 2. Setup Instructions

#### **For Windows**
1. Navigate to the project folder.
2. Install dependencies:
   ```bash
   pip install pygame
   ```
3. Run:
   ```bash
   python main.py
   ```

#### **For macOS / Linux**
1. Install Pygame:
   ```bash
   pip3 install pygame
   ```
2. Run:
   ```bash
   python3 main.py
   ```

---

## 🎮 Controls

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

## 🏗️ Technical Architecture

- **Maze Generation**: Recursive Backtracking (DFS-based carving).
- **UI Engine**: Pygame (Dynamic scaling & real-time rendering).
- **Data Structures**: 
  - Queues (BFS)
  - Stacks (DFS)
  - Priority Queues/Heaps (Dijkstra & A*)

---

## 📜 License
Distributed under the MIT License.

**Made with ❤️ for AI Enthusiasts**
