# 호텔

INF = int(1e9)

C, N = map(int, input().split())
data = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
dp = [0] + [INF] * (C + 100)

for cost, customers in data:
    for i in range(customers, C+100):
        dp[i] = min(dp[i-customers] + cost, dp[i])

print(min(dp[C:]))
