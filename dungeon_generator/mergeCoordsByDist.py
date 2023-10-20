

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

        if abs(x_distance) <= 10 and abs(y_distance) <= 10:
            # If distances are less than or equal to 10, merge the coordinates at the halfway point
            new_x = round((current_coord[1] + prev_coord[1]) / 2)
            new_y = round((current_coord[0] + prev_coord[0]) / 2)
            merged_coords[-1] = [new_y, new_x]
        else:
            # Otherwise, keep the current coordinate as is
            merged_coords.append(current_coord)

    return merged_coords


