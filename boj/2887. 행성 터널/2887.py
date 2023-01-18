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

parent = [x for x in range(N)]
graph = [list(map(int, sys.stdin.readline().rstrip().split())) + [i] for i in range(N)]
edges = []

for i in range(3):
    s = sorted(graph, key=lambda x: x[i])
    for j in range(N-1):
        edges.append((s[j][3], s[j+1][3], abs(s[j][i]-s[j+1][i])))

edges.sort(key=lambda x:x[2])

result = 0
for edge in edges:
    a, b, cost = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
