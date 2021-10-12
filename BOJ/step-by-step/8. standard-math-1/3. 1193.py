# 1193 분수찾기

import math

X = int(input())
n = math.ceil((-1 + math.sqrt(1+8*X))/2)

if n % 2 == 0:
    row = n - (n*(n+1)//2 - X)
    col = 1 + (n*(n+1)//2 - X)
else:
    row = 1 + (n*(n+1)//2 - X)
    col = n - (n*(n+1)//2 - X)
print(f'{row}/{col}')