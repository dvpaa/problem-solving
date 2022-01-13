# 1010 다리 놓기

dp = [[0] * (n+1) for n in range(31)]
dp[1][0], dp[1][1] = 1, 1
for i in range(2, 31):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
for _ in range(int(input())):
    N, M = map(int, input().split())
    print(dp[M][N])