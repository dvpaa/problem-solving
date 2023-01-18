# 10989 수 정렬하기 3

import sys
N = int(sys.stdin.readline())
data = [0] * 10001
for _ in range(N):
    i = int(sys.stdin.readline())
    data[i] += 1
for i in range(1, 10001):
    if data[i] != 0:
        for _ in range(data[i]):
            print(i)