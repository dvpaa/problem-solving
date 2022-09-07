# 1697 숨바꼭질

from collections import deque

N, K = map(int, input().split())
graph = [0] * 100001

def bfs(graph, K):
    queue = deque([N])
    while queue:
        x = queue.popleft()
        if x == K:
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000:
                if graph[nx] == 0:
                    graph[nx] = graph[x] + 1
                    queue.append(nx)
bfs(graph, K)
print(graph[K])