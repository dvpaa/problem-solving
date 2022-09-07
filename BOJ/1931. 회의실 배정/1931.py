# 1931 회의실 배정

N = int(input())
data = sorted([list(map(int, input().split())) for _ in range(N)], key= lambda x:(x[1], x[0]))
cnt = 1
end = data[0][1]
for i in range(1, N):
    if data[i][0] >= end:
        cnt += 1
        end = data[i][1]
print(cnt)