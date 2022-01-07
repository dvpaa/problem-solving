# 10814 나이순 정렬

N = int(input())
datas = []
for i in range(N):
    age, name = input().split()
    datas.append((int(age), name, i))
datas.sort(key= lambda x: (x[0], x[2]))
for data in datas:
    print(data[0], data[1])