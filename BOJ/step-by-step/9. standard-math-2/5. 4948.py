# 4948 베르트랑 공준

import math

N = 123456
array = [True for i in range((2*N)+1)]
array[1] = False
for i in range(2,int(math.sqrt(2*N))+1):
    if array[i]:
        j = 2
        while i*j <= 2*N:
            array[i*j] = False
            j += 1
while True:
    n = int(input())
    if not n:
        break
    cnt = 0
    for i in range(n+1,(2*n)+1):
        if array[i]:
            cnt += 1
    print(cnt)