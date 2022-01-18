# 11401 이항 계수 3

def exp(a, b):
    if b == 0:
        return 1
    if b % 2 == 1:  # 홀수이면
        return (exp(a, b//2) ** 2 * a) % p
    else:
        return (exp(a, b//2) ** 2) % p

N, K = map(int, input().split())
p = 1000000007
dp = [1] * (N+1)

for i in range(2, N+1):
    dp[i] = (i * dp[i-1]) % p

A = dp[N]
B = dp[N-K] * dp[K] % p

print(A * (exp(B, p-2) % p) % p)