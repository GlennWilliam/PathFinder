import pygame
import sys
import random
from collections import deque
import time

# Initialize Pygame
pygame.init()

# Constants
TILE_SIZE = 40
GRID_WIDTH = 10
GRID_HEIGHT = 10
SCREEN_WIDTH = TILE_SIZE * GRID_WIDTH
SCREEN_HEIGHT = TILE_SIZE * GRID_HEIGHT
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0) # Color for grid lines
RED = (255, 0, 0) # Color for obstacles
YELLOW = (255, 255, 0)  # Color for start point
BLUE = (0, 0, 255)  # Color for the end point
GREEN = (0, 255, 0)  # Color for path
GRAY = (200, 200, 200)  # Color for visited cells

# Calculate the number of obstacles (25% of the grid)
total_cells = GRID_WIDTH * GRID_HEIGHT
num_obstacles = int(total_cells * 0.25)

# Generate random positions for obstacles
obstacle_positions = set()
while len(obstacle_positions) < num_obstacles:
    x = random.randint(0, GRID_WIDTH - 1) * TILE_SIZE
    y = random.randint(0, GRID_HEIGHT - 1) * TILE_SIZE
    obstacle_positions.add((x, y))

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("20x20 Tile Grid")

# Variables to store start and end points
start_point = None
end_point = None

def draw_grid(path=[], visited=set()):
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            if (x, y) in obstacle_positions:
                pygame.draw.rect(screen, RED, rect)  # Fill the obstacle tile
            elif (x, y) == start_point:
                pygame.draw.rect(screen, YELLOW, rect)  # Fill the start point tile
            elif (x, y) == end_point:
                pygame.draw.rect(screen, GREEN, rect)  # Fill the end point tile
            elif (x, y) in path:
                pygame.draw.rect(screen, BLUE, rect)  # Fill the path tile
            elif (x, y) in visited:
                pygame.draw.rect(screen, GRAY, rect)  # Fill the visited nodes
            else:
                pygame.draw.rect(screen, WHITE, rect)  # Fill the normal tile
            pygame.draw.rect(screen, BLACK, rect, 1)  # Draw the outline

def bfs(start, end):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()
        if current == end:
            break

        x, y = current
        neighbors = [(x + TILE_SIZE, y), (x - TILE_SIZE, y), (x, y + TILE_SIZE), (x, y - TILE_SIZE)]
        for neighbor in neighbors:
            if (0 <= neighbor[0] < SCREEN_WIDTH and 0 <= neighbor[1] < SCREEN_HEIGHT and
                neighbor not in obstacle_positions and neighbor not in visited):
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current

                # Visualize the search process
                draw_grid(visited=visited)
                pygame.display.flip()
                time.sleep(0.1)  # Add delay for visualization

    path = []
    if end in parent:
        while end:
            path.append(end)
            end = parent[end]
        path.reverse()
    return path, visited

def main():
    global start_point, end_point
    clock = pygame.time.Clock()
    visited = set()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos # Get the mouse position
                x = (x // TILE_SIZE) * TILE_SIZE 
                y = (y // TILE_SIZE) * TILE_SIZE 
                if (x, y) not in obstacle_positions:
                    if start_point is None:
                        start_point = (x, y)
                    elif end_point is None:
                        end_point = (x, y)

        if start_point and end_point:
            path, visited = bfs(start_point, end_point)
            if path:  # Check if a path was found
                draw_grid(path, visited)
                pygame.display.flip()
                break  # Stop the loop once the path is found
        else:
            draw_grid(visited=visited)
        pygame.display.flip()
        clock.tick(90) # Limit the frame rate to 60 FPS

    # Keep the window open after finding the path
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(60)

if __name__ == "__main__":
    main()