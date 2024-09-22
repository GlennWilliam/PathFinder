from collections import deque

# DFS algorithm to find a path in a graph
# The graph is represented as an adjacency list
# The graph is a dictionary where the key is the node and the value is a list of neighbors
# The algorithm returns a path from the start node to the goal node
# If no path is found, it returns None
# The algorithm uses a stack to explore the graph in a depth-first manner

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs_path(self, start, goal):
        visited = set()  # Set to keep track of visited nodes
        stack = [(start, [start])]  # Stack to explore the graph

        while stack:
            (vertex, path) = stack.pop()  # Get the next vertex and path
            if vertex not in visited:  # Check if the vertex has been visited
                if vertex == goal:  # Check if we have reached the goal
                    return path
                visited.add(vertex)  # Mark the vertex as visited
                for neighbor in self.graph.get(vertex, []):  # Add neighbors to the stack
                    stack.append((neighbor, path + [neighbor]))
        return None

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')
    g.add_edge('C', 'E')
    g.add_edge('D', 'E')

    start = 'A'
    goal = 'E'
    path = g.dfs_path(start, goal)
    if path:
        print(f"Path from {start} to {goal} is: {' -> '.join(path)}")
    else:
        print(f"No path found from {start} to {goal}")