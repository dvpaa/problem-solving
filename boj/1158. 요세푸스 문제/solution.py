from collections import deque

N, K = map(int, input().split())
q = deque([x for x in range(1, N+1)])

result = []
cnt = 1
while q:
    if cnt % K == 0:
        result.append(q.popleft())
    else:
        q.append(q.popleft())
    
    cnt += 1

print("<", end="")    
print(*result, sep=", ", end="")
print(">")
