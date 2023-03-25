n = int(input())
dp = [4] * (n+1)
dp[0] = 0

for i in range(1, n+1):
    for j in range(int(i**0.5), 0, -1):
        dp[i] = min(1 + dp[i-j**2], dp[i])
print(dp[-1])
