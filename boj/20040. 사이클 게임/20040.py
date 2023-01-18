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


n, m = map(int, input().split())

parent = [x for x in range(n)]

cycle = False

for i in range(1, m + 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        print(i)
        break
    union_parent(parent, a, b)

if not cycle:
    print(0)
