# 1978 소수 찾기

import math

def isprime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

N = int(input())
array = list(map(int, input().split()))
print(len([x for x in array if isprime(x)]))