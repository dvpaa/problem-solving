# 4386 별자리 만들기

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

n = int(input())
stars = [tuple(map(float, input().split())) for _ in range(n)]
parent = [x for x in range(n)]
edges = []
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = stars[i]
        x2, y2 = stars[j]
        cost = ((x1-x2) ** 2 + (y1-y2) ** 2) ** 0.5
        edges.append((i,j,cost))
edges.sort(key = lambda x: x[2])
result = 0
for edge in edges:
    a, b, cost = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
print(round(result, 2))