# 11444 피보나치 수 6

def met_mul(A: list, B: list) -> list:
    N = len(A)
    C = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            for l in range(N):
                C[i][j] += A[i][l] * B[l][j]
            C[i][j] %= 1000000007
    return C

def met_exp(A: list, B: int) -> list:
    N = len(A)
    if B == 1:
        return A
    else:
        temp = met_exp(A, B//2)
        if B % 2 == 0:
            return met_mul(temp, temp)
        else:
            return met_mul(met_mul(temp, temp), A)

n = int(input())

A = [[1, 1], [1, 0]]
result = met_exp(A, n)
print(result[0][1])