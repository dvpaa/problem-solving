# 9372 상근이의 여행

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

for _ in range(int(input())):
    N, M = map(int, input().split())
    parent = [x for x in range(N+1)]
    edges = []
    for __ in range(M):
        edges.append(tuple(map(int, input().split())))
    result = 0
    for edge in edges:
        a, b = edge
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += 1
    print(result)