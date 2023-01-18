import heapq
import sys

INF = int(1e9)

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
distance = [INF] * (N + 1)
graph = [[] for i in range(N + 1)]
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))

A, B = map(int, sys.stdin.readline().rstrip().split())


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))


dijkstra(A)
print(distance[B])
