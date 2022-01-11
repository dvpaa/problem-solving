# 2579 계단 오르기

n = int(input())
data = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)
dp[1] = data[1]
if n > 1:
    dp[2] = data[1] + data[2]
for i in range(3, n+1):
    dp[i] = max(dp[i-3] + data[i-1], dp[i-2]) + data[i]
print(dp[n])