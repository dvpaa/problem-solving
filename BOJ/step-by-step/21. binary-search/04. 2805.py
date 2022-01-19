# 2805 나무 자르기

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)
while start <= end:
    mid = (start + end) // 2
    s = sum([i-mid if i > mid else 0 for i in trees])
    if s >= M:
        start = mid+1
    else:
        end = mid-1
print(end)