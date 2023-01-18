# 11047 동전 0

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins = coins[::-1]
result = 0
for coin in coins:
    result += K // coin
    K = K % coin
    if K == 0:
        break
print(result)