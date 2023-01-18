from collections import deque

N = int(input())
graph = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    graph[r - 1][c - 1] = 1

L = int(input())
operations = {int(a): b for a, b in [list(input().split()) for _ in range(L)]}

dx = [0, 1, 0, -1]  # 동 남 서 북
dy = [1, 0, -1, 0]  # 동 남 서 북

d = 0  # 초기 방향 설정
x, y = 0, 0  # 초기 좌표 설정
cnt = 1
snake = deque([(x, y)])

while True:
    # 규칙 1
    nx = x + dx[d]
    ny = y + dy[d]
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        break
    elif (nx, ny) in snake:
        break
    else:
        x, y = nx, ny
        snake.append((x, y))

        # 규칙 2
        if graph[x][y] == 1:
            graph[x][y] = 0
        # 규칙 3
        else:
            snake.popleft()

    if cnt in operations:
        if operations[cnt] == 'L':
            d = (d + 3) % 4
        elif operations[cnt] == 'D':
            d = (d + 1) % 4
    cnt += 1

print(cnt)
