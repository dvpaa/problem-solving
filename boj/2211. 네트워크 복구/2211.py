import sys
import heapq

INF = int(1e9)

N, M = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for i in range(N+1)]
distance = [INF] * (N+1)

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

path = [[] for i in range(N+1)]


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


dijkstra(1)
result = [p[-2:] for p in path if len(p) >= 2]
print(len(result))
for i in result:
    print(*i)
