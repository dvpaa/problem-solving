# 11659 구간 합 구하기 4

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
datas = [-1] + list(map(int, input().split()))

sums = [0] * (N+1)

for i in range(1, N+1):
    sums[i] = sums[i-1] + datas[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(sums[j] - sums[i-1])