
# main.py

import pygame
import random

import smlRoom
import medRoom
import lrgRoom

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

def fillWithBase(arr):

        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                arr[row][col] = 'e'

# def pasteSectors(spatArr, sectArr):
#      for row in spatArr:
#           for col in spatArr:


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

def spawnSectors(num):
    pointCloud = []
    for i in range(num):
        randSize = random.randint(0, 2)
        if randSize == 0:
            sector1 = medRoom.gen_MedSector(dungeon, random.randint(0, 80), random.randint(0, 80))
            pointCloud.append(sector1['origin'])
        if randSize == 1:
            sector2 = lrgRoom.gen_LrgSector(dungeon, random.randint(0, 60), random.randint(0, 60))
            pointCloud.append(sector2['origin'])
        if randSize == 2:
            sector3 = smlRoom.gen_SmlSector(dungeon, random.randint(0, 90), random.randint(0, 90))
            pointCloud.append(sector3['origin'])
             

          



#####################################################################################################
fillWithBase(dungeon)
spawnSectors(3)
draw_elements()
#print(sector1)
#print(dungeon)

######################################################################################################

# Main loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
