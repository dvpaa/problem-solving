# 11051 이항 계수 2

N, K = map(int, input().split())
dp = [[0] * (n+1) for n in range(1001)]
dp[1][0], dp[1][1] = 1, 1
for i in range(2, N+1):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
print(dp[N][K] % 10007)