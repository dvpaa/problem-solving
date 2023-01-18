# 1504 특정한 최단 경로

import sys
import heapq
imput = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
dis_1 = [INF] * (N+1)
dis_v1 = [INF] * (N+1)
dis_v2 = [INF] * (N+1)

for _ in range(E):
    a, b ,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int, input().split())

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(1, dis_1)
dijkstra(v1, dis_v1)
dijkstra(v2, dis_v2)

dist = min(dis_1[v1]+dis_v1[v2]+dis_v2[N], dis_1[v2]+dis_v2[v1]+dis_v1[N])

if dist >= INF:
    print(-1)
else:
    print(dist)