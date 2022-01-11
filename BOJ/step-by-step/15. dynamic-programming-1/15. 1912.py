# 1912 연속합

n = int(input())
a = list(map(int, input().split()))
dp = [0] * n
dp[0] = a[0]
for i in range(n):
    if dp[i-1] >= 0:
        dp[i] = dp[i-1] + a[i]
    else:
        dp[i] = a[i]
print(max(dp))