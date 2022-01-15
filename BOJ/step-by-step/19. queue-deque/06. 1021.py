# 1021 회전하는 큐

from collections import deque

N, M = map(int, input().split())
datas = list(map(int, input().split()))
q = deque([x for x in range(1, N+1)])
cnt = 0
for data in datas:
    while True:
        if q[0] == data:
            q.popleft()
            break
        else:
            if q.index(data) < len(q)/2:
                while q[0] != data:
                    q.append(q.popleft())
                    cnt += 1
            else:
                while q[0] != data:
                    q.appendleft(q.pop())
                    cnt += 1
print(cnt)