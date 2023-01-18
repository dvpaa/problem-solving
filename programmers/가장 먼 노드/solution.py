import heapq

def solution(n, edge):
    INF = int(1e9)
    distance = [INF] * (n+1)
    graph = [[] for x in range(n+1)]
    for e in edge:
        graph[e[0]].append((e[1], 1))
        graph[e[1]].append((e[0], 1))

    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    m = -1
    for i in range(1, n+1):
        if distance[i] != INF:
            m = max(m, distance[i])
    return distance.count(m)
