# 이중 우선순위 큐

import heapq
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    min_heap = []
    max_heap = []
    for __ in range(int(input())):
        oper = input().rstrip().split()

        if oper[0] == "I":
            common_list = [int(oper[1]), True]
            heapq.heappush(min_heap, [int(oper[1]), common_list])
            heapq.heappush(max_heap, [-int(oper[1]), common_list])

        elif oper[0] == "D":
            if oper[1] == "1":
                while max_heap:
                    max_val = heapq.heappop(max_heap)
                    if max_val[1][1]:
                        max_val[1][1] = False
                        break

            elif oper[1] == "-1":
                while min_heap:
                    min_val = heapq.heappop(min_heap)
                    if min_val[1][1]:
                        min_val[1][1] = False
                        break

    flag = True
    while max_heap:
        val = heapq.heappop(max_heap)
        if val[1][1]:
            print(val[1][0], end=" ")
            flag = False
            break

    while min_heap:
        val = heapq.heappop(min_heap)
        if val[1][1]:
            print(val[1][0])
            break

    if flag:
        print("EMPTY")
