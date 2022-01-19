# 1654 랜선 자르기

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
datas = [int(input()) for _ in range(K)]

start = 1
end = max(datas)

while start <= end:
    mid = (start+end) // 2
    s = 0
    for data in datas:
        s += data // mid
    
    if s >= N:
        start = mid + 1
    else:
        end = mid - 1


print(end)