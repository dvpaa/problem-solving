# 1780 종이의 개수

import sys

N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt_0, cnt_1, cnt_2 = 0, 0, 0


def paper(x, y, n):
    global cnt_0, cnt_1, cnt_2
    standard = data[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if data[i][j] != standard:
                paper(x, y, n // 3)
                paper(x, y + (n // 3), n // 3)
                paper(x, y + (2 * (n // 3)), n // 3)
                paper(x + (n // 3), y, n // 3)
                paper(x + (n // 3), y + (n // 3), n // 3)
                paper(x + (n // 3), y + (2 * (n // 3)), n // 3)
                paper(x + (2 * (n // 3)), y, n // 3)
                paper(x + (2 * (n // 3)), y + (n // 3), n // 3)
                paper(x + (2 * (n // 3)), y + (2 * (n // 3)), n // 3)
                return
    if standard == -1:
        cnt_0 += 1
        return
    elif standard == 0:
        cnt_1 += 1
    else:
        cnt_2 += 1
        return

paper(0, 0, N)
print(cnt_0, cnt_1, cnt_2, sep='\n')