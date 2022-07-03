import sys
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

diameter = [-1] * (n + 1)


def dfs(start, dia):
    for i in graph[start]:
        if diameter[i[0]] == -1:
            diameter[i[0]] = dia + i[1]
            dfs(i[0], dia+i[1])


diameter[1] = 0
dfs(1, 0)
node = diameter.index(max(diameter))

diameter = [-1] * (n + 1)
diameter[node] = 0
dfs(node, 0)

print(max(diameter))
