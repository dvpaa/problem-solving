# 2606 바이러스

from collections import deque

def bfs(graph, start, visted):
    queue = deque([start])
    visited[start] = True
    cnt = 0
    while queue:
        v = queue.popleft()
        for i in range(1, n+1):
            if not visted[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt

n = int(input())
m = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    A, B = map(int, input().split())
    graph[A][B] = 1
    graph[B][A] = 1

print(bfs(graph, 1, visited))