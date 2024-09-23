# Dijkstra and A* Pathfinding Visualizer
# PathFinder

This repository contains a Pygame-based visualization tool for demonstrating several path-finding algorithms. The algorithms included are:

1. **BFS (Breadth-First Search)**
2. **DFS (Depth-First Search)**
3. **Dijkstra's Algorithm**
4. **A* (A-Star)**

## Features

1. **Algorithm Files**:
  - `algorithm.py`: Contains the core algorithm logic.
  - `algorithm_visualizer.py`: Contains the Pygame-based visualization logic.

2. **Interactive Visualization**:
  - Users can interactively visualize how different algorithms explore the graph and find the optimal path.
  - The visualizer highlights the explored areas in real-time, showing the differences in search patterns between the algorithms.

## BFS and DFS

For BFS and DFS visualizer:
- Users can place the start and end points.
- Obstacles are generated randomly and automatically.

![BFS and DFS Visualization](https://github.com/user-attachments/assets/e1986558-3446-4b8c-9894-48fe14640efb)

- **Yellow**: Start point
- **Blue**: End point
- **Green**: Path

## Dijkstra and A*

The grid is represented as a 2D map, where each cell has a weight that determines the cost of moving through that cell. The weight influences how different algorithms find the optimal path.

![Dijkstra and A* Visualization 1](https://github.com/user-attachments/assets/5b882720-d3c0-4923-ac8b-f7899bfdec9a)
![Dijkstra and A* Visualization 2](https://github.com/user-attachments/assets/ae6ce817-ad6e-4d36-9c77-0cc159c3222d)

## Usage

1. **Clone the Repository**:
  ```sh
  git clone https://github.com/GlennWilliam/PathFinder.git
  ```

2. **Install Necessary Packages**:
  ```sh
  pip3 install pygame
  ```

3. **Run the Visualizer**:
  ```sh
  python3 algorithm_visualizer.py
  ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Contact

For any questions or suggestions, please open an issue or contact the repository owner.
