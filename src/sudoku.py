from utils import check_repetition, get_zone_arrays, generate_mask, apply_mask, generate_matrix


class Sudoku:

    def __init__(self, opened_fields_number):
        n = 3
        self.matrix = generate_matrix()
        self.mask = generate_mask(opened_fields_number)
        self.game_over = False
        apply_mask(self.matrix, self.mask)

    def show_matrix(self):
        for i in range(9):
            for j in range(9):
                if self.matrix[i][j] == 0:
                    print('_', end=' ')
                else:
                    print(self.matrix[i][j], end=' ')
            print()

    def set_matrix(self, matrix):
        self.matrix = matrix

    def check_correctness(self):
        arrays = get_zone_arrays(self.matrix)
        result = True
        for arr in arrays:
            if not check_repetition(arr):
                result = False
        return result

    def is_game_over(self):
        tmp = True
        for row in self.matrix:
            if row.__contains__(0):
                tmp = False
        self.game_over = tmp
        if self.game_over:
            self.show_matrix()
            print("Well done, buddy!")

    def make_move(self, x: int, y: int, number: int):
        if x < 1 or x > 9:
            print("Invalid x coordinate value")
        elif y < 1 or y > 9:
            print("Invalid y coordinate value")
        elif number < 1 or number > 9:
            print("Fuck you")
        else:
            tmp = self.matrix[x - 1][y - 1]
            self.matrix[x - 1][y - 1] = number
            if not self.check_correctness():
                self.matrix[x - 1][y - 1] = tmp
                print("Something is wrong")
            self.is_game_over()

    def play(self):
        while not self.game_over:
            self.is_game_over()
            a, b, c = map(int, input().split())
            self.make_move(a, b, c)
