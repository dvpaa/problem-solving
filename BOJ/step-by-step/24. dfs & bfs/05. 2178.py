# 2178 미로탐색

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b, graph, distance):
    queue = deque([(a, b)])
    distance[a][b] = 1
    graph[a][b] = -1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = -1
                    distance[nx][ny] = min(distance[x][y] + 1, distance[nx][ny])

INF = int(1e9)
N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
distance = [[INF] * M for _ in range(N)]

bfs(0, 0, graph, distance)
print(distance[N-1][M-1])