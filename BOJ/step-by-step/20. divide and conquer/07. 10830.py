# 10830 행렬 제곱

def met_mul(A: list, B: list) -> list:
    N = len(A)
    C = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            for l in range(N):
                C[i][j] += A[i][l] * B[l][j]
            C[i][j] %= 1000
    return C

def met_exp(A: list, B: int) -> list:
    N = len(A)
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A
    else:
        temp = met_exp(A, B//2)
        if B % 2 == 0:
            return met_mul(temp, temp)
        else:
            return met_mul(met_mul(temp, temp), A)

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

result = met_exp(A, B)
for i in range(N):
    for j in range(N):
        print(result[i][j], end = ' ')
    print()