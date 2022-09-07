# 1655 가운데를 말해요

import heapq
import sys
input = sys.stdin.readline

left_heap = []
right_heap = []
for i in range(1, int(input())+1):
    x = int(input())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -x)
    else:
        heapq.heappush(right_heap, x)
    if right_heap and (-left_heap[0] > right_heap[0]):
        left = heapq.heappop(right_heap)
        right = -heapq.heappop(left_heap)
        heapq.heappush(left_heap, -left)
        heapq.heappush(right_heap, right)
    print(-left_heap[0])