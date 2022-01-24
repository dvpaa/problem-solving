# 9370 미확인 도착지

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance = [INF for _ in range(n+1)]
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
    return distance

for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for __ in range(n+1)]

    for __ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    
    targets = sorted([int(input()) for __ in range(t)])

    dis1 = dijkstra(s)
    dis2 = dijkstra(g)
    dis3 = dijkstra(h)

    for target in targets:
        if dis1[target] == dis1[g]+dis2[h]+dis3[target] or dis1[target] == dis1[h]+dis3[g]+dis2[target]:
            print(target, end = ' ')
    print()