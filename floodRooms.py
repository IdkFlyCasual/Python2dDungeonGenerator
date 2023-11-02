





def roomMapper(arr):

    room = {
        'cells' : []
    }

    visited = []


    for row in arr:

        for col in arr:
            surroundingCells = {
                                'left' : arr[row][col-1],
                                'right' : arr[row][col+1],
                                'top' : arr[row-1][col],
                                'bottom' : arr[row+1][col],
                            }
            visited.append([row, col])

            if arr[row][col] == 'c1':
                room['cells'].append([row, col])

                for cell in room['cells']:

                    for val in surroundingCells.values():
                        if val == 'c1':
                            room['cells'].append(val)
