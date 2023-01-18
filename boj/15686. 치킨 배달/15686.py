from itertools import combinations

N, M = map(int, input().split())
datas = [list(map(int, input().split())) for _ in range(N)]

chick_pos = [(x, y) for x in range(N) for y in range(N) if datas[x][y] == 2]
home_pos = [(x, y) for x in range(N) for y in range(N) if datas[x][y] == 1]

result = 50000
for chick in combinations(chick_pos, M):
    temp = 0
    for home in home_pos:
        temp += min([abs(home[0]-i[0]) + abs(home[1]-i[1]) for i in chick])
    result = min(result, temp)

print(result)
