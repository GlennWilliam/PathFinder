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

    def heuristic(self, node, goal):
        # Example heuristic: Manhattan distance for grid-based graphs
        # For simplicity, assuming node and goal are tuples (x, y)
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    def a_star_shortest_path(self, start, goal):
        priority_queue = [(0, start, [])]  # (f_cost, node, path)
        g_costs = {start: 0}
        f_costs = {start: self.heuristic(start, goal)}
        shortest_paths = {start: [start]}

        while priority_queue:
            (current_f_cost, current_node, path) = heapq.heappop(priority_queue)

            if current_node == goal:
                return path + [current_node]

            for neighbor, weight in self.graph.get(current_node, []):
                tentative_g_cost = g_costs[current_node] + weight
                if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g_cost
                    f_costs[neighbor] = tentative_g_cost + self.heuristic(neighbor, goal)
                    heapq.heappush(priority_queue, (f_costs[neighbor], neighbor, path + [current_node]))
                    shortest_paths[neighbor] = path + [current_node]

        return None

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge((0, 0), (1, 0), 1)
    g.add_edge((0, 0), (0, 1), 4)
    g.add_edge((1, 0), (1, 1), 2)
    g.add_edge((0, 1), (1, 1), 1)
    g.add_edge((0, 1), (0, 2), 3)
    g.add_edge((1, 1), (0, 2), 1)

    start = (0, 0)
    goal = (0, 2)
    path = g.a_star_shortest_path(start, goal)
    if path:
        print(f"Shortest path from {start} to {goal} is: {' -> '.join(map(str, path))}")
    else:
        print(f"No path found from {start} to {goal}")