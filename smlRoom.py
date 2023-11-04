
# medRoom.py


import random

def gen_SmlSector(arr, yStart, xStart):

    sector = {
        'origin': [yStart+5, xStart+5],
        'layout': [],
        'style': 'none'
    }

    # Constants
    WALK_POINTS = []
    GRID_SIZE = 10

    GRID_COLS = GRID_SIZE
    GRID_ROWS = GRID_SIZE

    # Generate a 2D array to represent the sector grid
    smlSector = [[None for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]

    def roomBuilder(arr, dArr):


        h = random.randrange(3, 10)
        w = random.randrange(3, 10)
        longestDim = h
        if w > h:
            longestDim = w
        randStartI = random.randrange(0, len(arr)- longestDim)
        randStartJ = random.randrange(0, len(arr)- longestDim)

        centerI = round(h / 2)
        centerJ = round(w / 2)

        WALK_POINTS.append([randStartI + centerI, randStartJ + centerJ])

        for i in range(randStartI, randStartI + h):
            for j in range(randStartJ, randStartJ + w):
                arr[i][j] = 'floor'
                dArr[yStart+i][xStart+j] = 'floor'




        ###############################################################################


    # Fill the dungeon grid with cells (wall, b1, floor)
    def fillWithBase(arr):

        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                arr[row][col] = 'e'

    def generateRooms(num):

        for i in range(num):
            roomBuilder(smlSector, arr)

    ################################

    fillWithBase(smlSector)
    generateRooms(5)

    #################################

    return sector
