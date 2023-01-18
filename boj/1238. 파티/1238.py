import heapq
import sys

INF = int(1e9)

N, M, X = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for i in range(N + 1)]

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))


def dijkstra(start):
    distance = [INF] * (N + 1)
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

    return distance


dist_x = dijkstra(X)
result = [-1]
for i in range(1, N + 1):
    dist_i = dijkstra(i)
    result.append(dist_i[X] + dist_x[i])

print(max(result))
