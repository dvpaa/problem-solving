# 11866 요세푸스 문제 0

from collections import deque

N, K = map(int, input().split())
q = deque([x for x in range(1, N+1)])
result = []
i = 0
while q:
    if i == K-1:
        result.append(q.popleft())
        i = 0
    else:
        i += 1
        n = q.popleft()
        q.append(n)
print(f"<{', '.join(map(str, result))}>")