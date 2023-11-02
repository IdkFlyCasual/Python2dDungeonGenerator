
# medRoom.py


import random

def gen_MedSector(arr, yStart, xStart):

    sector = {
        'origin': [yStart+10, xStart+10],
        'layout': [],
        'style': 'none'
    }

    # Constants
    WALK_POINTS = []
    GRID_SIZE = 20

    GRID_COLS = GRID_SIZE
    GRID_ROWS = GRID_SIZE

    # Generate a 2D array to represent the sector grid
    medSector = [[None for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]

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
            layRow = []
            for j in range(randStartJ, randStartJ + w):
                arr[i][j] = 'floor'
                dArr[yStart+i][xStart+j] = 'floor'
                layRow.append(i)
                layRow.append(j)

            sector['layout'].append(layRow)

    def merge_coordinates(coordinates):
        # Sort the coordinates based on x values
        sorted_coords = sorted(coordinates, key=lambda coord: coord[1])

        # Initialize a list to store merged coordinates
        merged_coords = [sorted_coords[0]]

        for i in range(1, len(sorted_coords)):
            prev_coord = merged_coords[-1]
            current_coord = sorted_coords[i]

            # Calculate the x and y distances
            x_distance = current_coord[1] - prev_coord[1]
            y_distance = current_coord[0] - prev_coord[0]

            if abs(x_distance) <= 5 and abs(y_distance) <= 5:
                # If distances are less than or equal to 10, merge the coordinates at the halfway point
                new_x = round((current_coord[1] + prev_coord[1]) / 2)
                new_y = round((current_coord[0] + prev_coord[0]) / 2)
                merged_coords[-1] = [new_y, new_x]
            else:
                # Otherwise, keep the current coordinate as is
                merged_coords.append(current_coord)

        return merged_coords

    def checkPath(arr):

        #############################################################################################################
        #
        #paths is structured [ [[yCoorA], [yCoorB]], [[xCoorA], [xCoorB]], [[yCoorA], [yCoorB]], [[xCoorA], [xCoorB]] ]
        #                                         ^^^                                          ^^^
        #                                     first path                                 subsequent path
        #############################################################################################################

        paths = []
        i = 0
        while i < len(arr) -1:
            for j in range(i, len(arr)):

                #check distance between walking points
                if j != i:

                    if abs(arr[i][0] - arr[j][0]) > 5 and abs(arr[i][1] - arr[j][1]) > 5:
                        path = []

                        path.append([arr[i][0], arr[j][0]])

                        path.append([arr[i][1], arr[j][1]])

                        paths.append(path)
            i+=1
        # print(paths, '    ---->| PATHS')
        return paths


        ###############################################################################

    # use spatial array with this func
    #     vvvvv
    def walkPath(pths, spatial_array, dArr):
        for i in range(len(pths)):


            ya = pths[i][0][0]
            yb = pths[i][0][1]

            xa = pths[i][1][0]
            xb = pths[i][1][1]

            yStep = ya
            xStep = xa

            for y in range(abs(ya - yb - 1)):
                if ya > yb:

                    if yStep > 0 and yStep < len(spatial_array):
                        yStep -= 1
                        if spatial_array[yStep][xStep] != 'floor':
                            spatial_array[yStep][xStep] = 'floor'
                            dArr[yStep+yStart][xStep+xStart] = 'floor'
                if ya < yb:

                    if yStep > 1 and yStep < len(spatial_array):
                        yStep += 1
                        if spatial_array[yStep][xStep] != 'floor':
                            spatial_array[yStep][xStep] = 'floor'
                            dArr[yStep+yStart][xStep+xStart] = 'floor'

            for x in range(abs(xa - xb)):
                if xa > xb:

                    if xStep > 0 and xStep < len(spatial_array[yStep]):
                        xStep -= 1
                        if spatial_array[yStep][xStep] != 'floor':
                            spatial_array[yStep][xStep] = 'floor'
                            dArr[yStep+yStart][xStep+xStart] = 'floor'

                if xa < xb:

                    if xStep > 0 and xStep < len(spatial_array[yStep]):
                        xStep += 1
                        if spatial_array[yStep][xStep] != 'floor':
                            spatial_array[yStep][xStep] = 'floor'
                            dArr[yStep+yStart][xStep+xStart] = 'floor'

    # Fill the dungeon grid with cells (wall, b1, floor)
    def fillWithBase(arr):

        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                arr[row][col] = 'e'

    def generateRooms(num):

        for i in range(num):
            roomBuilder(medSector, arr)

    def generateHalls():

        coords = WALK_POINTS
        origins = merge_coordinates(coords)
        paths = checkPath(origins)
        print(paths)
        walkPath(paths, medSector, arr)

    ################################

    fillWithBase(medSector)
    generateRooms(10)
    generateHalls()

    #################################

    return sector
