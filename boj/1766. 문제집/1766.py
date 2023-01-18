import heapq
import sys

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    indegree[b] += 1

result = []
q = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(q, i)


def topology_sort():
    if len(result) == N:
        return

    while q:
        val = heapq.heappop(q)
        result.append(val)

        for i in graph[val]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i)

    print(*result)


topology_sort()
