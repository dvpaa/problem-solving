# 10816 숫자 카드 2

from bisect import bisect_left, bisect_right


N = int(input())
arr = sorted(list(map(int, input().split())))
M = int(input())
targets = list(map(int, input().split()))

for target in targets:
    print(bisect_right(arr, target) - bisect_left(arr, target), end = ' ')