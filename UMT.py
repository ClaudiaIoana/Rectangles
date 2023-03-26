"""
The program determines the number of rectangles using given coordinates.
It determines the coordinates by using two of them and seeing if the coordinates that help form a rectangle are present
in the given list of coordinates.
"""


def nb_rectangles(coordinates):
    # number of coordinates
    nb_rect = 0
    coor = coordinates

    # use 2 coordinates and determine the other two
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            # we select 2 sets of coordinates
            if coordinates[i][0] != coordinates[j][0] and coordinates[i][1] != coordinates[j][1]:
                if [coordinates[i][0], coordinates[j][1]] in coor and [coordinates[j][0], coordinates[i][1]] in coor:
                    nb_rect = nb_rect + 1

    # in the program a rectangle will be found 4 times, using different start coordinates,
    # so we divide by 4 to eliminate the duplicates
    return int(nb_rect/4)


if __name__ == '__main__':
    coordirantes = []
    f = open("input", "r")
    for i in f:
        i = i.split()
        x = int(i[0])
        y = int(i[1])
        coordirantes.append([x, y])

    print(nb_rectangles(coordirantes))