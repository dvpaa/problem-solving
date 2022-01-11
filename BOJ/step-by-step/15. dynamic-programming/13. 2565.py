# 2565 전깃줄

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
A.sort()
dp = [1] * N
for i in range(N):
    for j in range(i):
        if A[i][1] > A[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))