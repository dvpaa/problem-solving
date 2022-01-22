# 1012 유기농 배추

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b, graph):
    queue = deque([(a, b)])
    graph[a][b] = -1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N and 0 <= ny < M) and (graph[nx][ny] == 1):
                queue.append((nx, ny))
                graph[nx][ny] = -1

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j, graph)
                cnt += 1
    print(cnt)