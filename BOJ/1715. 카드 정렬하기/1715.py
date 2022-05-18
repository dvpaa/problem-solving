import heapq
import sys

N = int(sys.stdin.readline().strip())
datas = []

for i in range(N):
    heapq.heappush(datas, int(sys.stdin.readline().strip()))

cnt = 0
while True:
    if len(datas) == 1:
        break

    a = heapq.heappop(datas)
    b = heapq.heappop(datas)
    cnt += (a + b)
    heapq.heappush(datas, a + b)

print(cnt)
