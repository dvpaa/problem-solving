# 1929 소수 구하기

M, N = map(int, input().split())
table = [True] * (N+1)
table[1] = False
for i in range(2, int(N ** 0.5) + 1):
    if table[i]:
        j = 2
        while i*j <= N:
            table[i*j] = False
            j += 1
for i in range(M, N+1):
    if table[i]:
        print(i)