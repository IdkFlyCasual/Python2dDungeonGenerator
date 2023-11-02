import pygame
#import random
import roomGen
import mergeCoordsByDist
import hallGen



# Constants
GRID_SIZE = 20
GRID_WIDTH = 800
GRID_HEIGHT = 800
GRID_COLS = GRID_WIDTH // GRID_SIZE
GRID_ROWS = GRID_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
LIGHT_GREY = (192, 192, 192)
RED = (192, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((GRID_WIDTH, GRID_HEIGHT))

# Generate a 2D array to represent the dungeon grid
dungeon = [[None for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]

# Fill the dungeon grid with cells (wall, b1, floor)
def fillWithBase(arr):

    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            arr[row][col] = 'e'

def generateRooms(num):

    for i in range(num):
        roomGen.roomBuilder(dungeon)


def generateHalls():

    coords = roomGen.walkPoints
    # origins = mergeCoordsByDist.merge_coordinates(coords)
    paths = hallGen.checkPath(coords)
    hallGen.walkPath(paths, dungeon)


# Draw the shit
def draw_elements():

    for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                if dungeon[row][col] == 'e':
                    color = BLACK
                if dungeon[row][col] == 'wall':
                    color = GREY
                if dungeon[row][col] == 'floor':
                    color = LIGHT_GREY
                if dungeon[row][col] == 'wp':
                    print(' ---> walkpoint found at  > ', row, 'x', col)
                    color = RED

                pygame.draw.rect(screen, color, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))



#####################################################################################################


fillWithBase(dungeon)
generateRooms(10)
#roomGen.boolCleanup(dungeon)
generateHalls()
draw_elements()

######################################################################################################

# Main loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
