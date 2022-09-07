# 11279 최대 힙

import heapq
import sys
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if arr:
            print(-(heapq.heappop(arr)))
        else:
            print(0)
    else:
        heapq.heappush(arr, -x)