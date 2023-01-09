# 1, 2, 3 더하기

import sys

input = sys.stdin.readline


def dfs(i):
    global n
    if i > n:
        return

    dp[i] += 1
    for j in range(1, 4):
        dfs(i + j)


for _ in range(int(input())):
    n = int(input())
    dp = [0] * (n + 1)
    dfs(0)
    print(dp[n])