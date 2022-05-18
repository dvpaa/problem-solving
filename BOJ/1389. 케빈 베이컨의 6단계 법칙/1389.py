INF = int(1e9)

N, M = map(int, input().split())

graph = [[0] * (N + 1) for i in range(N + 1)]
path = [[INF] * (N + 1) for i in range(N + 1)]

for i in range(1, N+1):
    path[i][i] = 0

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    path[a][b] = 1
    path[b][a] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                continue

            if graph[i][k] == 1 and graph[k][j] == 1:
                if path[i][k] + path[k][j] < path[i][j]:
                    graph[i][j] = 1
                    graph[j][i] = 1
                    path[i][j] = path[i][k] + path[k][j]
                    path[j][i] = path[j][k] + path[k][i]


sum_path = [sum(p[1:]) for p in path[1:]]
result = [(idx+1, val) for (idx, val) in enumerate(sum_path) if val != 0]
result.sort(key=lambda x: (x[1], x[0]))

print(result[0][0])
