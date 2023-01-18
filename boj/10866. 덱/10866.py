# 10866 덱

import sys
from collections import deque

q = deque()
for _ in range(int(sys.stdin.readline())):
    com = sys.stdin.readline().split()
    if com[0] == 'push_front':
        q.appendleft(int(com[1]))
    elif com[0] == 'push_back':
        q.append(int(com[1]))
    elif com[0] == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif com[0] == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif com[0] == 'size':
        print(len(q))
    elif com[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif com[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif com[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)