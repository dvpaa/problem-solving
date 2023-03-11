# 1074 Z

N, r, c = map(int, input().split())

def recursion_search(n: int, row: int, col: int, cnt: int):
    if n == 0:
        print(cnt)
        return

    half_size = 2 ** (n - 1)
    add_size = half_size * half_size

    if r < row + half_size:
        if c < col + half_size:
            recursion_search(n - 1, row, col, cnt)
        else:
            recursion_search(n - 1, row, col + half_size, cnt + add_size)

    else:
        if c < col + half_size:
            recursion_search(n - 1, row + half_size, col, cnt + (add_size * 2))
        else:
            recursion_search(n-1, row + half_size, col + half_size, cnt + (add_size * 3))


recursion_search(N, 0, 0, 0)