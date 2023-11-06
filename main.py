
# main.py

import pygame
import random

import walkSectors
import basalisk

import smlRoom
import medRoom
import lrgRoom

# Constants
GRID_SIZE = 4
GRID_WIDTH = 800
GRID_HEIGHT = 800
GRID_COLS = GRID_WIDTH // GRID_SIZE
GRID_ROWS = GRID_HEIGHT // GRID_SIZE

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
LIGHT_GREY = (192, 192, 192)
RED = (192, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((GRID_WIDTH, GRID_HEIGHT))

# Generate a 2D array to represent the dungeon grid
dungeon = [[None for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]

# create empty list for sectors
sectors = []

def fillWithBase(arr):

        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                arr[row][col] = 'e'

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

    for i in range(num):
        randSize = random.randint(1, 100)
        placed = False

        if randSize < 30:
            attempts = 0
            while attempts < 10 and placed == False:
                randRow = random.randint(0, 190)
                randCol = random.randint(0, 190)

                # Check if the sector overlaps with any existing sectors
                overlap = False
                for existing_sector in sectors:
                    distance = ((randRow - existing_sector['origin'][0])**2 +
                                (randCol - existing_sector['origin'][1])**2)**0.5
                    if distance <= existing_sector['bound'] + 5 + 2:
                        overlap = True
                        break

                if not overlap:
                    # If there is no overlap, add the sector to the list
                    sector = smlRoom.gen_SmlSector(dungeon, randRow, randCol)
                    sectors.append(sector)
                    placed = True
                attempts += 1

        if randSize < 80:
            attempts = 0
            while attempts < 10 and placed == False:
                randRow = random.randint(0, 180)
                randCol = random.randint(0, 180)

                # Check if the sector overlaps with any existing sectors
                overlap = False
                for existing_sector in sectors:
                    distance = ((randRow - existing_sector['origin'][0])**2 +
                                (randCol - existing_sector['origin'][1])**2)**0.5
                    if distance <= existing_sector['bound'] + 10 + 2:
                        overlap = True
                        break

                if not overlap:
                    # If there is no overlap, add the sector to the list
                    sector = medRoom.gen_MedSector(dungeon, randRow, randCol)
                    sectors.append(sector)
                    placed = True
                attempts += 1

        if randSize < 100:
            attempts = 0
            while attempts < 10 and placed == False:
                randRow = random.randint(0, 160)
                randCol = random.randint(0, 160)

                # Check if the sector overlaps with any existing sectors
                overlap = False
                for existing_sector in sectors:
                    distance = ((randRow - existing_sector['origin'][0])**2 +
                                (randCol - existing_sector['origin'][1])**2)**0.5
                    if distance <= existing_sector['bound'] + 20 + 3:
                        overlap = True
                        break

                if not overlap:
                    # If there is no overlap, add the sector to the list
                    sector = lrgRoom.gen_LrgSector(dungeon, randRow, randCol)
                    sectors.append(sector)
                    placed = True
                attempts += 1

def getKeyValues(arr, key):
    values = []
    for dict in arr:
        values.append(dict[key])
    return values

def walkhalls(paths, arr):
    pths = walkSectors.checkPath(paths)
    walkSectors.walkPath(pths, arr)

#####################################################################################################
fillWithBase(dungeon)
spawnSectors(50)
origins = getKeyValues(sectors, 'origin')
walkhalls(origins, dungeon)
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
