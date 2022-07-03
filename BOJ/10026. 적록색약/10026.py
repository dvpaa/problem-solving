import sys
sys.setrecursionlimit(10**9)

N = int(input())
graph = [input() for _ in range(N)]

visited_color = [[False] * N for _ in range(N)]
visited_blind = [[False] * N for _ in range(N)]

color = {'R': 0, 'G': 1, 'B': 2}
blind = {'R': 1, 'G': 1, 'B': 2}

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = [0, 0]


def dfs(x: int, y: int, visited: list, color_type: dict):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and color_type[graph[x][y]] == color_type[graph[nx][ny]]:
                    dfs(nx, ny, visited, color_type)


def count(visited: list, color_type: dict):
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                result[color_type['R']] += 1
                dfs(i, j, visited, color_type)


count(visited_color, color)
count(visited_blind, blind)

print(*result)
