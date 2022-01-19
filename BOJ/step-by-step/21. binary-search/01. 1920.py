# 1920 수 찾기

def binary_search(array: list, target: int, start: int, end: int) -> bool:
    if start > end:
        return False
    mid = (start + end) // 2
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
arr = list(map(int, input().split()))

l = len(A)-1
for target in arr:
    if binary_search(A, target, 0, l):
        print(1)
    else:
        print(0)