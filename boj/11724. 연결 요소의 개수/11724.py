# 11724

import sys
input = sys.stdin.readline


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


N, M = map(int, input().split())
parent = [x for x in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    union_parent(parent, u, v)

result = set()
for i in range(1, N+1):
    result.add(find_parent(parent, i))

print(len(result))
