# 2231 분해합

N = int(input())
result = False
for i in range(1, N+1):
    S = i + sum(map(int, str(i)))
    if S == N:
        print(i)
        result = True
        break
if not result:
    print(0)