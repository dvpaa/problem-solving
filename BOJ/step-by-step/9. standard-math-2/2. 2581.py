# 2581 소수

import math

def isprime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

M = int(input())
N = int(input())

array = [x for x in range(M, N+1) if isprime(x)]
print(-1) if not array else print(sum(array), array[0], sep = '\n')