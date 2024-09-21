from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs_shortest_path(self, start, goal):
        visited = set()
        queue = deque([(start, [start])])

        while queue:
            (vertex, path) = queue.popleft()
            if vertex not in visited:
                if vertex == goal:
                    return path
                visited.add(vertex)
                for neighbor in self.graph.get(vertex, []):
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