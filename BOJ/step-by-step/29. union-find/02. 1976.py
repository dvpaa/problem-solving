# 1976 여행 가자

def find_parent(parent, x):
    if parent[x] != x:
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

for i in range(N):
    city = list(map(int, input().split()))
    for j in range(N):
        if city[j] == 1:
            union_parent(parent, i+1, j+1)

plans = list(map(int, input().split()))
plan = True
for i in range(M-1):
    if find_parent(parent, plans[i]) != find_parent(parent, plans[i+1]):
        plan = False
        break

print('YES') if plan else print('NO')