# 10830 행렬 제곱

def met_mul(A: list, B: list, N: int) -> list:
    C = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            for l in range(N):
                C[i][j] += A[i][l] * B[l][j]
            C[i][j] %= 1000
    return C

def met_exp(A: list, B: int, N: int) -> list:
    if B == 1:
        return A
    elif B == 2:
        return met_mul(A, A, N)
    else:
        temp = met_exp(A, B//2, N)
        if B % 2 == 0:
            return met_mul(temp, temp, N)
        else:
            return met_mul(met_mul(temp, temp, N), A, N)

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

result = met_exp(A, B, N)
for i in range(N):
    for j in range(N):
        print(result[i][j], end = ' ')
    print()