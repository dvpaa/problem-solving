# 2164 카드2

from collections import deque

N = int(input())
q = deque([N-x for x in range(N)])
while True:
    if len(q) == 1:
        break
    q.pop()
    n = q.pop()
    q.appendleft(n)
print(q.pop())