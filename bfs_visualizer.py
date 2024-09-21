import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
TILE_SIZE = 40
GRID_WIDTH = 20
GRID_HEIGHT = 15
SCREEN_WIDTH = TILE_SIZE * GRID_WIDTH
SCREEN_HEIGHT = TILE_SIZE * GRID_HEIGHT
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0) # Color for grid lines
RED = (255, 0, 0) # Color for obstacles
YELLOW = (255, 255, 0)  # Color for start point
GREEN = (0, 255, 0)  # Color for end point

# Calculate the number of obstacles (30% of the grid)
total_cells = GRID_WIDTH * GRID_HEIGHT
num_obstacles = int(total_cells * 0.3)

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

def draw_grid():
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            if (x, y) in obstacle_positions:
                pygame.draw.rect(screen, RED, rect)  # Fill the obstacle tile
            elif (x, y) == start_point:
                pygame.draw.rect(screen, YELLOW, rect)  # Fill the start point tile
            elif (x, y) == end_point:
                pygame.draw.rect(screen, GREEN, rect)  # Fill the end point tile
            else:
                pygame.draw.rect(screen, WHITE, rect)  # Fill the normal tile
            pygame.draw.rect(screen, BLACK, rect, 1)  # Draw the outline

def main():
    global start_point, end_point
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos # Get the mouse position
                x = (x // TILE_SIZE) * TILE_SIZE # Round down to the nearest multiple of TILE_SIZE
                y = (y // TILE_SIZE) * TILE_SIZE # Round down to the nearest multiple of TILE_SIZE
                if (x, y) not in obstacle_positions:
                    if start_point is None:
                        start_point = (x, y)
                    elif end_point is None:
                        end_point = (x, y)

        draw_grid()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()