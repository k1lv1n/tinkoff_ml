from random import randint, shuffle


def check_repetition(array):
    d = dict()
    for a in array:
        try:
            d[a] += 1
        except KeyError:
            d[a] = 1
    res = True
    for element in d.items():
        if element[0] != 0 and element[1] > 1:
            res = False
    return res


def get_zone_arrays(matrix):
    zone_arrays = []
    for _ in range(27):
        zone_arrays.append([])
    for i in range(9):
        for j in range(9):
            zone_arrays[i].append(matrix[i][j])
            zone_arrays[9 + j].append(matrix[i][j])
            zone_arrays[18 + 3 * (i // 3) + (j // 3)].append((matrix[i][j]))
    return zone_arrays


def generate_mask(n):
    mask = [[0 for _ in range(9)] for _ in range(9)]
    if n > 81:
        raise ValueError
    ls = list(range(0, 81))
    shuffle(ls)
    for i in range(n):
        mask[ls[i] // 9][ls[i] % 9] = 1
    return mask


def apply_mask(matrix, mask):
    for i in range(9):
        for j in range(9):
            if mask[i][j] == 0:
                matrix[i][j] = 0


def transpose(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i < j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def swap_rows(matrix):
    r1, r2 = randint(0, 8), randint(0, 8)
    while r1 // 3 != r2 // 3:
        r1, r2 = randint(0, 8), randint(0, 8)
    for j in range(9):
        matrix[r1][j], matrix[r2][j] = matrix[r2][j], matrix[r1][j]


def swap_cols(matrix):
    transpose(matrix)
    swap_rows(matrix)
    transpose(matrix)


def swap_areas_row(matrix):
    area_row_1, area_row_2 = randint(0, 2), randint(0, 2)
    if area_row_1 == area_row_2:
        pass
    if area_row_1 > area_row_2:
        area_row_1, area_row_2 = area_row_2, area_row_1
    k = (area_row_2 - area_row_1) * 3
    for i in range(9):
        for j in range(9):
            if i // 3 == area_row_2:
                matrix[i][j], matrix[i - k][j] = matrix[i - k][j], matrix[i][j]


def swap_areas_col(matrix):
    transpose(matrix)
    swap_areas_row(matrix)
    transpose(matrix)


def generate_matrix():
    n = 3
    base_matrix = [[int((i * n + i / n + j) % (n * n) + 1) for j in range(n * n)] for i in range(n * n)]
    if bool(randint(0, 1)):
        transpose(base_matrix)
    for _ in range(randint(0, 35)):
        swap_rows(base_matrix)
        swap_cols(base_matrix)
        swap_areas_row(base_matrix)
        swap_areas_col(base_matrix)
    return base_matrix
