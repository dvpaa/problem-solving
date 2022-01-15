# 1966 프린터 큐

from collections import deque

for _ in range(int(input())):
    N, M = map(int, input().split())
    data = deque(list(map(int, input().split())))
    check = deque([0 for _ in range(N)])
    check[M] = 1
    cnt = 0

    while True:
        if data[0] == max(data):
            cnt += 1
            if check[0] != 1:
                data.popleft()
                check.popleft()
            else:
                print(cnt)
                break
        else:
            data.append(data[0])
            check.append(check[0])
            data.popleft()
            check.popleft()