# 7562 나이트의 이동

from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(graph, target_x, target_y):
    while queue:
        x, y = queue.popleft()
        if (x, y) == (target_x, target_y):
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<l and 0<=ny<l:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

for _ in range(int(input())):
    l = int(input())
    x, y = map(int, input().split())
    target_x , target_y = map(int, input().split())
    graph = [[0]*l for __ in range(l)]
    queue = deque([(x, y)])
    bfs(graph, target_x, target_y)
    print(graph[target_x][target_y])