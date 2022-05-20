import sys

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
M = int(input())

parent = [x for x in range(N+1)]
edges = [tuple(map(int, sys.stdin.readline().rstrip().split())) for i in range(M)]
edges.sort(key=lambda x: x[2])

result = 0
for edge in edges:
    a, b, cost = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
