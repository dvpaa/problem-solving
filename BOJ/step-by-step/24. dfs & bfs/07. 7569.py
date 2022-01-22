# 7569 토마토

from collections import deque

dx = [-1, 1, 0, 0, 0, 0] # H
dy = [0, 0, 0, 0, -1, 1] # N
dz = [0, 0, -1, 1, 0, 0] # M

def bfs(graph):
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<H and 0<=ny<N and 0<=nz<M:
                if graph[nx][ny][nz] == 0:
                    queue.append((nx,ny,nz))
                    graph[nx][ny][nz] = graph[x][y][z] + 1

def search(graph):
    result = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 0:
                    result = 0
                    return result
                else:
                    result = max(graph[i][j][k], result)
    return result

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for __ in range(H)]
queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append((i,j,k))

bfs(graph)
print(search(graph)-1)