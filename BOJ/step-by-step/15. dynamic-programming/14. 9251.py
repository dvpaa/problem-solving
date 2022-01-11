# 9251 LCS

X = ' ' + input()
Y = ' ' + input()
dp = [[0] * len(Y) for _ in range(len(X))]
for i in range(1, len(X)):
    for j in range(1, len(Y)):
        if X[i] == Y[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])