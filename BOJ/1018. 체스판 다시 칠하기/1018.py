# 체스판 다시 칠하기

N, M = map(int, input().split())
graph = [input() for _ in range(N)]

stand = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
]

result = []

for i in range(N-7):
    for j in range(M-7):
        cnt = 0
        for k in range(8):
            for l in range(8):
                if graph[i+k][j+l] != stand[k][l]:
                    cnt += 1
        result.append(min(cnt, 64-cnt))

print(min(result))