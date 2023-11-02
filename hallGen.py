import random
import roomGen

# use coords array for this func
#      vvvvv
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
        for j in range(len(arr)):

            #check distance between walking points
            if j != i:

                if abs(arr[i][0] - arr[j][0]) < 25 and abs(arr[i][1] - arr[j][1]) < 25 and abs(arr[i][0] - arr[j][0]) > 15 and abs(arr[i][1] - arr[j][1]) > 15:
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
def walkPath(pths, spatial_array):
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
            if ya < yb:

                if yStep > 1 and yStep < len(spatial_array):
                    yStep += 1
                    if spatial_array[yStep][xStep] != 'floor':
                        spatial_array[yStep][xStep] = 'floor'

        for x in range(abs(xa - xb)):
            if xa > xb:

                if xStep > 0 and xStep < len(spatial_array[yStep]):
                    xStep -= 1
                    if spatial_array[yStep][xStep] != 'floor':
                        spatial_array[yStep][xStep] = 'floor'

            if xa < xb:

                if xStep > 0 and xStep < len(spatial_array[yStep]):
                    xStep += 1
                    if spatial_array[yStep][xStep] != 'floor':
                        spatial_array[yStep][xStep] = 'floor'
