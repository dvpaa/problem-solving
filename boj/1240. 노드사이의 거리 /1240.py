# 노드사이의 거리

import heapq

INF = int(1e9)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    distance[start][start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[start][now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[start][i[0]]:
                distance[start][i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


for i in range(1, N + 1):
    dijkstra(i)

for _ in range(M):
    a, b = map(int, input().split())
    print(distance[a][b])
