# 5430 AC

from collections import deque

for _ in range(int(input())):
    p = input()
    n = int(input())
    X = input()
    cnt_R = 0
    error = False

    X = list(X[1:-1].split(','))
    arr = deque([int(i) for i in X if i.isdigit()])
    for com in p:
        if com == 'R':
            cnt_R += 1
        else:
            if arr:
                if cnt_R % 2 == 1:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                error = True
                break
    if error:
        print('error')
    else:
        if cnt_R % 2 == 1:
            arr.reverse()
        print('[' + ','.join(map(str, list(arr))) + ']')