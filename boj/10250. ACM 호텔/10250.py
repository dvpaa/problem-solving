# 10250 ACM 호텔

from math import ceil
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    Y, X = N%H, ceil(N/H)
    if Y == 0: Y = H
    print(Y*100+X)