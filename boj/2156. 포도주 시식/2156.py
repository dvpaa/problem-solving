# 2156 포도주 시식

n = int(input())
data = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)
dp[1] = data[1]
if n > 1:
    dp[2] = sum(data[1:3])
for i in range(3, n+1):
    dp[i] = max(dp[i-3]+data[i-1]+data[i], dp[i-2]+data[i], dp[i-1])
print(max(dp))