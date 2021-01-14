from sudoku_src.sudoku import Sudoku

n = int(input("Количество известных клеток: "))
s = Sudoku(n)
s.solve()
