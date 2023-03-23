from collections import deque

n, m = map(int, input().split())
ladders = {}
snakes = {}
result = [int(1e9)] * 101

for _ in range(n):
    x, y = map(int, input().split())
    ladders[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    snakes[u] = v

q = deque([(1, 0)])

while q:
    node, cost = q.popleft()
    if cost >= result[node]:
        continue

    result[node] = min(result[node], cost)
    if node in snakes:
        q.append((snakes[node], result[node]))
        continue

    if node in ladders:
        q.append((ladders[node], result[node]))
    
    for i in range(1, min(100-node, 6)+1):
        q.append((node+i, result[node]+1))

print(result[100])
