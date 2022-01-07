# 2750 수 정렬하기
N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))
data.sort()
print(*data, sep= '\n')