# 큐
import sys
from collections import deque
input = sys.stdin.readline

q = deque([])

for _ in range(int(input())):
    S = input().rstrip().split()
    if S[0] == "push":
        q.append(int(S[1]))
    elif S[0] == "pop":
        print(q.popleft()) if q else print(-1)
    elif S[0] == "size":
        print(len(q))
    elif S[0] == "front":
        print(q[0]) if q else print(-1)
    elif S[0] == "back":
        print(q[-1]) if q else print(-1)
    elif S[0] == "empty":
        print(0) if q else print(1)
