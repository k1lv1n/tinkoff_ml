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
    if n == 0:
        return mask
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
    for _ in range(randint(0, 15)):
        swap_rows(base_matrix)
        swap_cols(base_matrix)
        swap_areas_row(base_matrix)
        swap_areas_col(base_matrix)
    return base_matrix


board = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]


def solve(bo):
    find = find_empty(bo)
    if not find:  # if find is None or False
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if valid(bo, num, (row, col)):
            bo[row][col] = num

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0:
            if i == 0:
                print(" ┎─────────┰─────────┰─────────┒")
            else:
                print(" ┠─────────╂─────────╂─────────┨")

        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" ┃ ", end=" ")

            if j == 8:
                print(bo[i][j], " ┃")
            else:
                print(bo[i][j], end=" ")

    print(" ┖─────────┸─────────┸─────────┚")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row, column

    return None


# solve(board)
# print_board(board)
