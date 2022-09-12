# 1005 ACM Craft

import sys
from collections import deque

for _ in range(int(sys.stdin.readline().rstrip())):
    N, K = map(int, sys.stdin.readline().rstrip().split())
    times = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    graph = [[] for __ in range(N + 1)]
    in_degree = [-1] + [0] * N
    dp = [0] * (N+1)

    for ___ in range(K):
        X, Y = map(int, sys.stdin.readline().rstrip().split())
        graph[X].append(Y)
        in_degree[Y] += 1
    W = int(sys.stdin.readline().rstrip())

    q = deque()
    for idx, val in enumerate(in_degree):
        if val == 0:
            dp[idx] = times[idx]
            q.append(idx)
    while q:
        prev = q.popleft()
        for next in graph[prev]:
            dp[next] = max(dp[next], dp[prev] + times[next])
            in_degree[next] -= 1
            if in_degree[next] == 0:
                q.append(next)
    print(dp[W])
