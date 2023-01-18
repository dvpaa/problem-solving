import collections

N = int(input())
graph = [[] for _ in range(N + 1)]
cost = [0] * (N + 1)
indegree = [0] * (N + 1)

for i in range(1, N + 1):
    datas = list(map(int, input().split()))
    cost[i] = datas[0]
    for x in datas[1:-1]:
        indegree[i] += 1
        graph[x].append(i)


def topology_sort():
    result = [0] * (N + 1)
    q = collections.deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result[now] += cost[now]

        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now])
            if indegree[i] == 0:
                q.append(i)

    print(*result[1:], sep='\n')


topology_sort()
