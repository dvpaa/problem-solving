N, M = map(int, input().split())
r, c, d = map(int, input().split())
datas = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
x, y = r, c
result = 0

while True:
    # 1
    if datas[x][y] == 0:
        datas[x][y] = -1
        result += 1

    # 2-a
    flag = False
    for i in range(4):
        d = 3 if d == 0 else d - 1
        nx = x + dx[d]
        ny = y + dy[d]
        if datas[nx][ny] == 0:
            x, y = nx, ny
            break
        if i == 3:
            flag = True
    # 2-b
    if flag:
        if datas[x-dx[d]][y-dy[d]] == 1:
            break
        else:
            x = x - dx[d]
            y = y - dy[d]

print(result)
