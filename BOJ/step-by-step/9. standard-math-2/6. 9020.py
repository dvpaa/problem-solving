# 9020 골드바흐의 추측

import math

N = 10000
array = [True for i in range((N)+1)]
array[1] = False
for i in range(2,int(math.sqrt(N))+1):
    if array[i]:
        j = 2
        while i*j <= N:
            array[i*j] = False
            j += 1
T = int(input())
for _ in range(T):
    n = int(input())
    result = []
    for i in range(1,(n//2)+1):
        if array[i] and array[n-i]:
            result.append([i,n-i])
    if len(result) > 1:
        temp = []
        for i in range(len(result)):
            temp.append(result[i][0]-result[i][1])
        print(result[temp.index(max(temp))][0],result[temp.index(max(temp))][1])
    else:
        print(result[0][0],result[0][1])