import heapq
import sys

INF = int(1e9)

N, M, K, X = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for i in range(N + 1)]
distance = [INF] * (N + 1)

for i in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    graph[A].append((B, 1))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))


dijkstra(X)
result = [idx for idx in range(1, N+1) if distance[idx] == K]
print(*result, sep='\n') if result else print(-1)
