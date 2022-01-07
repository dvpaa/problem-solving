# 2108 통계학
import sys
from collections import Counter

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(int(sys.stdin.readline()))
data.sort()
print(round(sum(data) / N))
print(data[N//2])
cnt = Counter(data).most_common(2)
if len(data) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(data[-1] - data[0])