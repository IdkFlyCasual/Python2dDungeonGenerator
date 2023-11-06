
def checkPath(arr):

    def getDistance(coor1, coor2):
        distY = abs(coor1[0] - coor2[0])
        distX = abs(coor1[1] - coor2[1])
        dist = distY
        if distX > distY:
            dist = distX
        return dist

    def getClosestPath(pth, pths):
        curr = 0
        for i in range(1, len(pths)):
            if getDistance(pth, pths[i]) < getDistance(pth, pths[curr]):
                curr = i
        return curr


    paths = []

    i = 0
    while i < len(arr):
        for j in range(i, len(arr)):

            #check distance between walking points
            distance = getDistance(arr[i], arr[j])
            if j != i:
                if distance < 40 and distance > 20:
                    path = []
                    path.append([arr[i][0], arr[j][0]])
                    path.append([arr[i][1], arr[j][1]])
                    paths.append(path)
        i+=1
    # print(paths, '    ---->| PATHS')
    return paths



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
