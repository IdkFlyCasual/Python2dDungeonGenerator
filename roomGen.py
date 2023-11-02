
import random

walkPoints = []


def roomBuilder(arr):


    h = random.randrange(5, 20)
    w = random.randrange(5, 20)
    longestDim = h
    if w > h:
        longestDim = w
    randStartI = random.randrange(0, len(arr)- longestDim)
    randStartJ = random.randrange(0, len(arr)- longestDim)

    centerI = round(h / 2)
    centerJ = round(w / 2)

    walkPoints.append([randStartI + centerI, randStartJ + centerJ])

    for i in range(randStartI, randStartI + h):
        for j in range(randStartJ, randStartJ + w):
            arr[i][j] = 'floor'

                # surrCells = {
                #     'topleft': arr[row-1][col-1],
                #     'top': arr[row-1][col],
                #     'topright': arr[row-1][col+1],
                #     'left': arr[row][col-1],
                #     'right': arr[row][col+1],
                #     'bottleft': arr[row+1][col-1],
                #     'bottom': arr[row+1][col-1],
                #     'bottright': arr[row+1][col+1]
                # }
            #print(i, 'x', j)

            # if i == randStartI or i == randStartI + h - 1:
            #     if arr[i][j] == 'e':
            #         arr[i][j] = 'wall'
            #     else:
            #         arr[i][j] = 'floor'
            # if j == randStartJ or j == randStartJ + w - 1:
            #     if arr[i][j] == 'e':
            #         arr[i][j] = 'wall'
            #     else:
            #         arr[i][j] = 'floor'
            # if j > randStartJ and j < randStartJ + w -1  and i > randStartI and i < randStartI + h -1:
            #     arr[i][j] = 'floor'

#     boolCleanup(arr)


# def boolCleanup(arr):
#     for row in range(len(arr)):
#         for col in range(len(arr[row])):
#             cell = arr[row][col]

#             if row == 0 or row == len(arr) - 1 and cell != 'e':
#                 cell = 'wall'
#             if col == 0 or col == len(arr[row]) - 1 and cell != 'e':
#                 cell = 'wall'

#             if row > 0 and row < len(arr) - 1 and col > -1 and col < len(arr[row]) - 1:

#                 if cell != 'e':
#                     if surrCells['top'] == 'e' and surrCells['bottom'] == 'wall':
#                         cell = 'wall'
#                     if surrCells['left'] == 'e' and surrCells['right'] == 'wall':
#                         cell = 'wall'
#                     if surrCells['bottom'] == 'e' and surrCells['top'] == 'wall':
#                         cell = 'wall'
#                     if surrCells['right'] == 'e' and surrCells['left'] == 'wall':
#                         cell = 'wall'
#                     if surrCells['top'] == 'wall' and surrCells['bottom'] == 'wall':
#                         cell = 'wall'
#                     if surrCells['left'] == 'wall' and surrCells['right'] == 'wall':
#                         cell = 'wall'

#                 valChecker = list(surrCells.values())

#                 if cell == 'floor' and valChecker.count('e') > 1:
#                     print('found it')
#                     arr[row][col] = 'wall'


###################################    Drop Shadow    #########################################
            # if surrCells['top'] == 'e' and cell == 'floor':
            #     #print('wall found')
            #     cell = 'wall'
            # if surrCells['top'] == 'e' and cell == 'floor':
            #     #print('wall found')
            #     cell = 'wall'
###############################################################################################
