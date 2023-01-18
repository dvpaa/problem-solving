# 1005 ACM Craft

import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    graph = [[] for __ in range(N + 1)]
    in_degree = [-1] + [0] * N  # 진입 차수 초기화
    dp = [0] * (N + 1)  # dp 테이블 초기화

    for ___ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        in_degree[Y] += 1
    W = int(input())

    q = deque()
    for idx, val in enumerate(in_degree):
        if val == 0:  # 진입 차수가 0이면 큐에 삽입
            dp[idx] = times[idx]  # 건물 건설에 걸리는 시간 확정
            q.append(idx)
    while q:
        prev = q.popleft()
        for next in graph[prev]:  # 연결된 노드 탐색
            dp[next] = max(dp[next], dp[prev] + times[next])  # 건물 건설에 걸리는 시간 업데이트
            in_degree[next] -= 1  # 진입 차수 -1
            if in_degree[next] == 0:  # 새롭게 진입 차수가 0이된 노드 큐에 삽입
                q.append(next)
    print(dp[W])
