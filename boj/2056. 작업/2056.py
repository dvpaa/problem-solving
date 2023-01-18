import collections

N = int(input())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
time = [0] * (N+1)

for i in range(1, N+1):
    datas = list(map(int, input().split()))
    time[i] = datas[0]
    for x in datas[2:]:
        indegree[i] += 1
        graph[x].append(i)


def topology_sort():
    result = [0] * (N+1)
    q = collections.deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result[now] += time[now]

        for x in graph[now]:
            indegree[x] -= 1
            result[x] = max(result[x], result[now])
            if indegree[x] == 0:
                q.append(x)

    print(max(result))


topology_sort()
