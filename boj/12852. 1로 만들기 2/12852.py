# 1로 만들기 2

INF = int(1e9)

N = int(input())

dp = [INF] * (N+1)
record = [[] for _ in range(N+1)]
dp[1] = 0

for i in range(1, N+1):
    if i+1 <= N:
        if dp[i] + 1 < dp[i + 1]:
            dp[i + 1] = dp[i] + 1
            record[i + 1].append(i)
    if i*2 <= N:
        if dp[i] + 1 < dp[i * 2]:
            dp[i * 2] = dp[i] + 1
            record[i * 2].append(i)
    if i*3 <= N:
        if dp[i] + 1 < dp[i * 3]:
            dp[i * 3] = dp[i] + 1
            record[i * 3].append(i)

print(dp[N])
result = []
i = N
while True:
    result.append(i)
    if i == 1:
        break
    i = record[i][-1]

print(*result)
