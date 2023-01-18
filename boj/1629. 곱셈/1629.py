# 1629 곱셈

A, B, C = map(int, input().split())

def mul(A, B, C):
    if B == 1:
        return A % C
    else:
        num = mul(A, B//2, C)
        if B % 2 == 0:
            return num * num % C
        else:
            return num * num * A % C

print(mul(A, B, C))