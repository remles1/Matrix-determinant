import copy


def la_place(matrix):
    var = copy.deepcopy(matrix)
    if len(var) == 2:
        return var[0][0] * var[1][1] - var[0][1] * var[1][0]

    g = -1
    det = 0

    for i in range(len(var)):
        g *= -1
        det += g * matrix[0][i] * la_place(scale_down(var, i))
    return det


def scale_down(matrix, i):
    var = copy.deepcopy(matrix)
    if len(var) > 2:
        var.pop(0)
        for x in range(len(var)):
            var[x].pop(i)
    return var


a = [[9, 4, 2, 3, 2, 7],
     [1, 3, 2, 2, 2, 5],
     [9, 9, 9, 3, 3, 6],
     [9, 9, 9, 4, 5, 7],
     [1, 2, 3, 5, 4, 5],
     [2, 6, 2, 3, 4, 1]]
print(la_place(a))
