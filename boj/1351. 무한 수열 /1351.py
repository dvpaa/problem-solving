# 무한 수열

N, P, Q = map(int, input().split())
A = dict()
A[0] = 1


def arr(i: int):
    if i in A:
        return A[i]
    A[i] = arr(i//P) + arr(i//Q)
    return A[i]


print(arr(N))
