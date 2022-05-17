import heapq
import sys

INF = int(1e9)

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)
path = [[] for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))

A, B = map(int, sys.stdin.readline().rstrip().split())


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start, start))

    while q:
        dist, now, prev = heapq.heappop(q)
        if distance[now] < dist:
            continue

        path[now] = path[prev] + [now]

        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0], now))


dijkstra(A)
print(distance[B])
print(len(path[B]))
print(*path[B])
