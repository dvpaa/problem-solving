# 7568 덩치

N = int(input())
data = []
for _ in range(N):
    x,y = map(int,input().split())
    data.append([x,y])
for i in range(N):
    a = 1
    for j in range(N):
        if i == j:
            continue
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            a += 1
    data[i].append(a)
for i in range(N):
    print(data[i][2],end = " ")