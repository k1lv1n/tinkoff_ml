import pickle
from copy import deepcopy

from sudoku_src.utils import check_repetition, get_zone_arrays, generate_mask, apply_mask, generate_matrix, find_empty


class Sudoku:

    def __init__(self, opened_fields_number):
        n = 3
        self.matrix = generate_matrix()
        self.mask = generate_mask(opened_fields_number)
        self.game_over = False
        self.solution = deepcopy(self.matrix)
        apply_mask(self.matrix, self.mask)

    def show_matrix(self):
        for i in range(9):
            if i % 3 == 0:
                if i == 0:
                    print(" ┎─────────┰─────────┰─────────┒")
                else:
                    print(" ┠─────────╂─────────╂─────────┨")

            for j in range(9):
                if j % 3 == 0:
                    print(" ┃ ", end=" ")

                if j == 8:
                    if self.matrix[i][j] != 0:
                        print(self.matrix[i][j], " ┃")
                    else:
                        print("*  ┃")
                else:
                    if self.matrix[i][j] != 0:
                        print(self.matrix[i][j], end=" ")
                    else:
                        print("*", end=" ")

        print(" ┖─────────┸─────────┸─────────┚")

    def is_possible(self, x, y, v):
        tmp_matrix = deepcopy(self.matrix)
        tmp_matrix[x][y] = v
        arrays = get_zone_arrays(tmp_matrix)
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
            if not self.is_possible(x - 1, y - 1, number):
                print("Something is wrong")
            else:
                print("Value was ", self.matrix[x - 1][y - 1])
                self.matrix[x - 1][y - 1] = number
                self.is_game_over()

    def save(self, name):
        name += ".pkl"
        with open(name, 'wb') as f:
            pickle.dump(self.matrix, f)

    def load(self, name):
        name += ".pkl"
        with open(name, 'rb') as f:
            self.matrix = pickle.load(f)

    def play(self):
        self.is_game_over()
        while not self.game_over:
            self.show_matrix()
            command = input()
            if command == "move":
                a, b, c = map(int, input().split())
                self.make_move(a, b, c)
            if command == "save":
                name = input("Name the game: ")
                self.save(name)
            if command == "load":
                name = input("Name of game: ")
                self.load(name)

    def solve(self):
        for i in range(9):
            for j in range(9):
                if self.matrix[i][j] == 0:
                    # print(i + 1, j + 1)
                    for k in range(1, 10):
                        if self.is_possible(i, j, k):
                            self.matrix[i][j] = k
                            self.show_matrix()
                            if find_empty(self.matrix) is None:
                                return True
                            if self.solve():
                                return True
                            self.matrix[i][j] = 0
                    return
