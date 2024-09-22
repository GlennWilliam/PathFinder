import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append((u, weight))  # Assuming undirected graph

    def dijkstra_shortest_path(self, start, goal):
        priority_queue = [(0, start, [])]  # (distance, node, path)
        shortest_distances = {start: 0}
        shortest_paths = {start: [start]}

        while priority_queue:
            (current_distance, current_node, path) = heapq.heappop(priority_queue)

            if current_node == goal:
                return path + [current_node]

            for neighbor, weight in self.graph.get(current_node, []):
                distance = current_distance + weight
                if neighbor not in shortest_distances or distance < shortest_distances[neighbor]:
                    shortest_distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor, path + [current_node]))
                    shortest_paths[neighbor] = path + [current_node]

        return None

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'D', 2)
    g.add_edge('C', 'D', 1)
    g.add_edge('C', 'E', 3)
    g.add_edge('D', 'E', 1)

    start = 'A'
    goal = 'E'
    path = g.dijkstra_shortest_path(start, goal)
    if path:
        print(f"Shortest path from {start} to {goal} is: {' -> '.join(path)}")
    else:
        print(f"No path found from {start} to {goal}")