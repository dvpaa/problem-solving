# 2667 단지번호붙이기

def dfs(x, y, n, graph):
    global cnt
    if 0 <= x < n and 0 <= y < n:
        if graph[x][y] == 1:
            graph[x][y] = -1
            cnt += 1
            dfs(x, y+1, n, graph)
            dfs(x, y-1, n, graph)
            dfs(x+1, y, n, graph)
            dfs(x-1, y, n, graph)


N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
result = []

for i in range(N):
    for j in range(N):
        cnt = 0
        if graph[i][j] == 1:
            dfs(i, j, N, graph)
            result.append(cnt)
result.sort()
print(len(result), *result, sep = '\n')