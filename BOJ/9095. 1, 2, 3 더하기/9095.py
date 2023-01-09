# 1, 2, 3 더하기

import sys

input = sys.stdin.readline

dp = [0] * 12


def dfs(i):
    if i > 11:
        return

    dp[i] += 1
    for j in range(1, 4):
        dfs(i + j)


dfs(0)

for _ in range(int(input())):
    n = int(input())
    print(dp[n])

