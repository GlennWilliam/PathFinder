import pygame as pg
from heapq import heappop, heappush

# Constants
TILE = 40
cols, rows = 19, 19
WIDTH, HEIGHT = cols * TILE, rows * TILE

# Initialize Pygame
pg.init()
sc = pg.display.set_mode([WIDTH, HEIGHT])
clock = pg.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Load the background image
background_image = pg.image.load('img.png')
background_image = pg.transform.scale(background_image, (WIDTH, HEIGHT))

# Grid
grid = [
    "1111111111111333333",
    "3333333333331333433",
    "4433333333331333333",
    "3333553334431333333",
    "3333555534431333333",
    "3443555553431333333",
    "3311111133331333433",
    "1115555111111333333",
    "1335553333341333433",
    "1335553334331333433",
    "1333333444331333333",
    "1344333333331111111",
    "1333333333333333333",
    "1344333333333333333",
    "1344333333333333433",
    "1333333443333333333",
    "11111133333333333333",
    "3333313333334333333",
    "3333313333333333433"
]

# Convert grid to a list of lists
grid = [list(map(int, row)) for row in grid]

def draw_grid():
    for y in range(rows):
        for x in range(cols):
            color = WHITE if grid[y][x] == 1 else GRAY
            pg.draw.rect(sc, color, (x * TILE, y * TILE, TILE, TILE), 1)

def dijkstra(start, end):
    pq = []
    heappush(pq, (0, start))
    distances = {start: 0}
    previous = {start: None}
    visited = set()

    while pq:
        current_distance, current_node = heappop(pq)
        visited.add(current_node)

        if current_node == end:
            break

        x, y = current_node
        neighbors = [(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
        for nx, ny in neighbors:
            if 0 <= nx < cols and 0 <= ny < rows and (nx, ny) not in visited:
                distance = current_distance + grid[ny][nx]
                if (nx, ny) not in distances or distance < distances[(nx, ny)]:
                    distances[(nx, ny)] = distance
                    heappush(pq, (distance, (nx, ny)))
                    previous[(nx, ny)] = current_node

        # Visualize the current state
        sc.blit(background_image, (0, 0))  # Draw the background image
        draw_grid()
        for node in visited:
            pg.draw.rect(sc, RED, (node[0] * TILE, node[1] * TILE, TILE, TILE), 5)
        pg.draw.rect(sc, GREEN, (start[0] * TILE, start[1] * TILE, TILE, TILE), 5)
        pg.draw.rect(sc, BLUE, (end[0] * TILE, end[1] * TILE, TILE, TILE), 5)
        pg.display.flip()
        clock.tick(10)

        # Handle events to keep the window responsive
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return []

    # Reconstruct path
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = previous[node]
    path.reverse()
    return path

def main():
    start = (5, 18)
    end = (18, 11)
    path = dijkstra(start, end)

    # Draw final path
    sc.blit(background_image, (0, 0))  # Draw the background image
    draw_grid()
    for node in path:
        pg.draw.rect(sc, GREEN, (node[0] * TILE, node[1] * TILE, TILE, TILE), 5)
    pg.display.flip()

    # Wait until the user closes the window
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        clock.tick(30)

    pg.quit()

if __name__ == "__main__":
    main()