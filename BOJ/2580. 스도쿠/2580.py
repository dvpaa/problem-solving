# 2580 스도쿠

import sys

sudoku = []
blank = []
breaker = True

for i in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i, j))


def solve(idx):
    global breaker
    if idx == len(blank):
        breaker = False
        for s in sudoku:
            print(*s)
        return

    x, y = blank[idx][0], blank[idx][1]
    for k in range(1, 10):
        if breaker and is_sudoku(x, y, k):
            sudoku[x][y] = k
            solve(idx+1)
            sudoku[x][y] = 0


def is_sudoku(row, col, val):
    for i in range(9):
        if sudoku[row][i] == val:
            return False

    for i in range(9):
        if sudoku[i][col] == val:
            return False

    nx = (row // 3) * 3
    ny = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[nx+i][ny+j] == val:
                return False

    return True


solve(0)
