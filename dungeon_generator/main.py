import pygame
#import random
import roomGen
import mergeCoordsByDist
import hallGen



# Constants
GRID_SIZE = 8
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

# Fill the dungeon grid with cells (a1, b1, c1)
def fillWithBase(arr):

    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            arr[row][col] = 'e'

def generateRooms(num):

    for i in range(num):
        roomGen.roomBuilder(dungeon)

def generateHalls():

    coords = roomGen.walkPoints
    origins = mergeCoordsByDist.merge_coordinates(coords)
    paths = hallGen.checkPath(origins)
    hallGen.walkPath(paths, dungeon)


# Draw the shit
def draw_elements():

    for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                if dungeon[row][col] == 'e':
                    color = BLACK
                if dungeon[row][col] == 'a1':
                    color = GREY
                if dungeon[row][col] == 'b1':
                    #print('wall found in window')
                    color = GREY
                if dungeon[row][col] == 'c1':
                    color = LIGHT_GREY
                if dungeon[row][col] == 'wp':
                    print(' ---> walkpoint found at  > ', row, 'x', col)
                    color = RED

                pygame.draw.rect(screen, color, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))



#####################################################################################################


fillWithBase(dungeon)
generateRooms(25)
generateHalls()
roomGen.hallCleanUp(dungeon)
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