# 1, 2, 3 더하기

import sys

input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    dp = [-1, 1, 2, 4]

    for i in range(4, n+1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

    print(dp[n])