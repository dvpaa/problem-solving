# 1764

N, M = map(int, input().split())
n_hear = {input() for _ in range(N)}
n_see = {input() for _ in range(M)}


inter = sorted(list(n_hear.intersection(n_see)))
print(len(inter))
print(*inter, sep='\n')
