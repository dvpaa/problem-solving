# 13549 숨바꼭질 3

import heapq

N, K = map(int, input().split())
INF = int(1e9)
distance = [INF] * 200001


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if now == K:
            break
        if distance[now] < dist:
            continue

        if 2*now < 200001:
            if dist < distance[2*now]:
                distance[2*now] = dist
                heapq.heappush(q, (dist, 2*now))

        if now-1 >= 0:
            if dist+1 < distance[now-1]:
                distance[now-1] = dist+1
                heapq.heappush(q, (dist+1, now-1))

        if now+1 < 200001:
            if dist+1 < distance[now+1]:
                distance[now+1] = dist+1
                heapq.heappush(q, (dist+1, now+1))


dijkstra(N)
print(distance[K])
