# 1260 DFS와 BFS

from collections import deque

def dfs(graph, v, visted):
    visted[v] = True
    print(v, end = ' ')
    for i in range(1, N+1):
        if not visted[i] and graph[v][i] == 1:
            dfs(graph, i, visted)

def bfs(graph, start, visted):
    queue = deque([start])
    visted[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in range(1, N+1):
            if not visted[i] and graph[v][i] == 1:
                queue.append(i)
                visted[i] = True

N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A][B] = 1
    graph[B][A] = 1

visted1 = [False] * (N+1)
visted2 = [False] * (N+1)

dfs(graph, V, visted1)
print()
bfs(graph, V, visted2)