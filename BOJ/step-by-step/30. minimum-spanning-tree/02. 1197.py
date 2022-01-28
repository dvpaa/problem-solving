# 1197 최소 스패닝 트리

import sys
input = sys.stdin.readline

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

V, E = map(int, input().split())
parent = [x for x in range(V+1)]
edges = []
for _ in range(E):
    edges.append(tuple(map(int, input().split())))
edges.sort(key = lambda x: x[2])

result = 0
for edge in edges:
    A, B, C = edge
    if find(parent, A) != find(parent, B):
        union(parent, A, B)
        result += C
print(result)