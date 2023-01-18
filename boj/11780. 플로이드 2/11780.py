import sys

INF = int(1e9)

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = [[INF] * (n + 1) for i in range(n + 1)]
path = [[[] for i in range(n + 1)] for j in range(n + 1)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if c < graph[a][b]:
        graph[a][b] = c
        path[a][b] = [a] + path[a][b][1:-1] + [b]

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue

            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                path[i][j] = path[i][k] + path[k][j][1:]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0)
        else:
            print(len(path[i][j]), *path[i][j], sep=' ')
