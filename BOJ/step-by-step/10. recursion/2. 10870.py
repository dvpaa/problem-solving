# 10870 피보나치 수 5

def arr(N:int) -> int:
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return arr(N-2) + arr(N-1)
n = int(input())
print(arr(n))