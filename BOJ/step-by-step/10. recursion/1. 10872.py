# 10872 팩토리얼

def fact(N:int) -> int:
    if N == 0:
        return 1
    return N*fact(N-1)
N = int(input())
print(fact(N))