# Dijkstra and A* Pathfinding Visualizer
This repository contains a Pygame-based visualization tool for demonstrating several path-finding algorithm. The algorithms are:
1. BFS (Breath-First Search)
2. DFS (Depth-First Search)
3. Dijkstra's
4. A* (A-Star)

# Features
1. Each algorithm has two files:
  1. algorithm.py for the core algorithm logic
  2. algorithm_visualizer.py for the Pygame-based visualization
2. Users can interactively visualize how different algorithms explore the graph and find the optimal path.
3. The visualizer highlights the explored areas in real-time, showing the difference in search patterns between the algorithms.

# BFS and DFS
For BFS and DFS visualizer: The user can place the start point and end point. Obstacles are generated randomly and automatically.

<img width="399" alt="Screenshot 2024-09-22 at 5 12 33 PM" src="https://github.com/user-attachments/assets/e1986558-3446-4b8c-9894-48fe14640efb">

- Yellow represents start point
- Blue represents end point
- Green represent the path

# Dijkstra and A*
The grid is represent ted as a 2D map, where each cell has a weight that determines the cost of moving through that cell. 
The weight influences how different algorithms find the optimal path.

<img width="757" alt="Screenshot 2024-09-22 at 5 19 04 PM" src="https://github.com/user-attachments/assets/5b882720-d3c0-4923-ac8b-f7899bfdec9a">
<img width="759" alt="Screenshot 2024-09-22 at 5 19 47 PM" src="https://github.com/user-attachments/assets/ae6ce817-ad6e-4d36-9c77-0cc159c3222d">
