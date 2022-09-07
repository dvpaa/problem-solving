# 13305 주유소

N = int(input())
length = list(map(int, input().split()))
cost = list(map(int, input().split()))
result = 0
mincost = cost[0]
for i in range(N-1):
    if mincost > cost[i]:
        mincost = cost[i]
    result += mincost * length[i]
print(result)