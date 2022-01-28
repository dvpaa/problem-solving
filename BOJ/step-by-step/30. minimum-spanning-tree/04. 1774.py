# 1774 우주신과의 교감

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [x for x in range(N+1)]
pos = [False] + [tuple(map(int, input().split())) for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    union(parent, a, b)
edges = []
for i in range(1, N+1):
    for j in range(i, N+1):
        x1, y1 = pos[i]
        x2, y2 = pos[j]
        cost = ((x1-x2) ** 2 + (y1-y2) ** 2) ** 0.5
        edges.append((i, j, cost))
edges.sort(key = lambda x: x[2])
result = 0
for edge in edges:
    a, b, c = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += c
print(f'{result:.2f}')