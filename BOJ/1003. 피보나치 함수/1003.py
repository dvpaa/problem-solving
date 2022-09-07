# 1003 피보나치 함수

dp = [[] for _ in range(41)]
dp[0], dp[1] = [1, 0], [0, 1] 
for i in range(2, 41):
    x = dp[i-1][0] + dp[i-2][0]
    y = dp[i-1][1] + dp[i-2][1]
    dp[i].append(x)
    dp[i].append(y)

for _ in range(int(input())):
    N = int(input())
    print(*dp[N])