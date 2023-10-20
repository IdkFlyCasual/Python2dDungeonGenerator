
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

            
            #print(i, 'x', j)

            if i == randStartI or i == randStartI + h - 1:
                if arr[i][j] == 'e':
                    arr[i][j] = 'a1'
                else:
                    arr[i][j] = 'c1'
            if j == randStartJ or j == randStartJ + w - 1:
                if arr[i][j] == 'e':
                    arr[i][j] = 'a1'
                else:
                    arr[i][j] = 'c1'
            if j > randStartJ and j < randStartJ + w -1  and i > randStartI and i < randStartI + h -1:
                arr[i][j] = 'c1'
    
    boolCleanup(arr)
    

def boolCleanup(arr):
    for row in range(len(arr)):
        for col in range(len(arr[row])):

            if row == 0 or row == len(arr) - 1 and arr[row][col] != 'e':
                arr[row][col] = 'a1'
            if col == 0 or col == len(arr[row]) - 1 and arr[row][col] != 'e':
                arr[row][col] = 'a1'

            if row > 0 and row < len(arr) - 1 and col > -1 and col < len(arr[row]) - 1:

                surroundingCells = [arr[row - 1][col - 1], arr[row - 1][col], arr[row - 1][col + 1], 
                                    arr[row][col - 1], arr[row][col + 1],
                                    arr[row + 1][col - 1], arr[row + 1][col], arr[row + 1][col + 1] ]
                if arr[row][col] != 'e':
                    if surroundingCells[1] == 'e' and surroundingCells[6] == 'a1':
                        arr[row][col] = 'a1'
                    if surroundingCells[3] == 'e' and surroundingCells[4] == 'a1':
                        arr[row][col] = 'a1'
                    if surroundingCells[6] == 'e' and surroundingCells[1] == 'a1':
                        arr[row][col] = 'a1'
                    if surroundingCells[4] == 'e' and surroundingCells[3] == 'a1':
                        arr[row][col] = 'a1'
                    if surroundingCells[1] == 'a1' and surroundingCells[6] == 'a1':
                        arr[row][col] = 'a1'
                    if surroundingCells[3] == 'a1' and surroundingCells[4] == 'a1':
                        arr[row][col] = 'a1'
                   
###################################    Drop Shadow    #########################################
                # if surroundingCells[1] == 'a1' and arr[row][col] == 'c1':
                #     #print('wall found')
                #     arr[row][col] = 'b1'
                # if surroundingCells[1] == 'e' and arr[row][col] == 'c1':
                #     #print('wall found')
                #     arr[row][col] = 'b1'
###############################################################################################

                if arr[row][col] == 'b1' and surroundingCells[1] == 'c1':
                    arr[row][col] = 'c1'


def hallCleanUp(arr):
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if row > 0 and row < len(arr) - 1 and col > -1 and col < len(arr[row]) - 1:

                surroundingCells = [arr[row - 1][col - 1], arr[row - 1][col], arr[row - 1][col + 1], 
                                    arr[row][col - 1], arr[row][col + 1],
                                    arr[row + 1][col - 1], arr[row + 1][col], arr[row + 1][col + 1] ]
                if arr[row][col] == 'e' and surroundingCells.count('c1') > 1:
                    arr[row][col] = 'a1'
                        
    