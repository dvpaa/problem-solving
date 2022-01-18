# 2740 행렬 곱셈

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

C = [[] for _ in range(N)]

for i in range(N):
    for j in range(K):
        s = 0
        for l in range(M):
            s += A[i][l] * B[l][j]
        C[i].append(s)

for c in C:
    print(*c)