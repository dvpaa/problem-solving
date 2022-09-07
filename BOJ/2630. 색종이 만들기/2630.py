# 2630 색종이 만들기

import sys

N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt_0, cnt_1 = 0, 0

def search_color(x, y, n):
    global cnt_0, cnt_1
    standard = data[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if data[i][j] != standard:
                search_color(x, y, n//2)
                search_color(x+(n//2), y, n//2)
                search_color(x+(n//2), y+(n//2), n//2)
                search_color(x, y+(n//2), n//2)
                return
    if standard == 0:
        cnt_0 += 1
        return
    else:
        cnt_1 += 1
        return

search_color(0, 0, N)
print(cnt_0, cnt_1, sep= '\n')