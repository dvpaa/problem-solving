# 11650 좌표 정렬하기

N = int(input())
datas = []
for _ in range(N):
    x, y = map(int, input().split())
    datas.append((x, y))
datas.sort(key= lambda x: (x[0],x[1]))
for data in datas:
    print(*data, sep=' ')