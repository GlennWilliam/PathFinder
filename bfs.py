from collections import deque

# BFS algorithm to find the shortest path in a graph
# The graph is represented as an adjacency list
# The graph is a dictionary where the key is the node and the value is a list of neighbors
# The algorithm returns the shortest path from the start node to the goal node
# If no path is found, it returns None
# The algorithm uses a queue to explore the graph in a breadth-first manner

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs_shortest_path(self, start, goal):
        visited = set() # Set to keep track of visited nodes
        queue = deque([(start, [start])]) # Queue to explore the graph

        while queue:
            (vertex, path) = queue.popleft() # Get the next vertex and path
            if vertex not in visited: # Check if the vertex has been visited
                if vertex == goal: # Check if we have reached the goal
                    return path
                visited.add(vertex) # Mark the vertex as visited
                for neighbor in self.graph.get(vertex, []): # Add neighbors to the queue
                    queue.append((neighbor, path + [neighbor])) 
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
    path = g.bfs_shortest_path(start, goal)
    if path:
        print(f"Shortest path from {start} to {goal} is: {' -> '.join(path)}")
    else:
        print(f"No path found from {start} to {goal}")