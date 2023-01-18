# 테트로미노

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]  # up, down, left, right on x
dy = [0, 0, -1, 1]  # up, down, left, right on y
result = 0


def dfs(x, y, sum_val, cnt):
    global result

    sub_result = sum_val + graph[x][y]
    if cnt == 4:
        result = max(result, sub_result)
        return

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, sub_result, cnt + 1)
                visited[nx][ny] = False


def none_dfs(x, y):
    global result
    for i in range(4):
        sum_val = graph[x][y]
        for j in range(3):
            direction = (i+j) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]

            if not (0 <= nx < N and 0 <= ny < M):
                break
            sum_val += graph[nx][ny]

        result = max(result, sum_val)


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 0, 1)
        visited[i][j] = False

        none_dfs(i, j)

print(result)
