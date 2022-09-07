# 2751 수 정렬하기2

import sys
imput = sys.stdin.readline
N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))
data.sort()
print(*data, sep= '\n')