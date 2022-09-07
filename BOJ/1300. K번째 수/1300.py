# K번째 수

N = int(input())
K = int(input())

start = 1
end = N ** 2

while start <= end:
    mid = (start + end) // 2
    s = 0
    for i in range(1, N+1):
        s += min(mid//i ,N)
    
    if s >= K:
        end = mid-1
    else:
        start = mid+1

print(start)