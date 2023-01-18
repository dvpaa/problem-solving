# 11651 좌표 정렬하기 2

N = int(input())
datas = []
for _ in range(N):
    x, y = map(int, input().split())
    datas.append((x, y))
datas.sort(key= lambda x: (x[1],x[0]))
for data in datas:
    print(*data, sep=' ')