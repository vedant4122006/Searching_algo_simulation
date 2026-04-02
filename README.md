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

### 1. System Requirements
- **Git** (to clone the repository)
- **Python 3.8+**
- **Operating System:** Windows, macOS, or Linux (GUI required)

### 2. Setup Instructions

#### **Step 1: Clone the Repository**
Open your terminal or command prompt and pull the code to your local machine:
```bash
git clone [https://github.com/vedant4122006/Searching_algo_simulation.git](https://github.com/vedant4122006/Searching_algo_simulation.git)
cd Searching_algo_simulation
```

#### **Step 2: Create a Virtual Environment**
It is highly recommended to isolate this project to avoid package conflicts.
- **Windows:**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
- **macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

#### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **Step 4: Run the Application**
- **Windows:**
  ```bash
  python main.py
  ```
- **macOS / Linux:**
  ```bash
  python3 main.py
  ```

---

### ⚠️ Common Errors & Troubleshooting

**1. `ModuleNotFoundError: No module named 'pygame'`**
- **Cause:** Pygame was not installed in the current environment.
- **Fix:** Ensure the virtual environment is active (you should see `(venv)` in your terminal). Re-run `pip install -r requirements.txt`.

**2. `pygame.error: No available video device`**
- **Cause:** This happens on Linux servers or WSL (Windows Subsystem for Linux) when no display output is detected.
- **Fix:** This simulation requires a GUI. If using WSL, ensure you have WSLg installed or an X-Server (like VcXsrv) running. Otherwise, run the project natively on Windows or macOS.

**3. `Scripts cannot be loaded...` (Windows PowerShell)**
- **Cause:** Security policy prevents running the activation script.
- **Fix:** Open PowerShell as Administrator and run:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

**4. `python` or `pip` is not recognized**
- **Cause:** Python is not added to your system PATH.
- **Fix:** Reinstall Python and ensure the "Add Python to PATH" checkbox is selected, or use `python3` and `pip3` commands instead.

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
