# 11399 ATM

N = int(input())
P = sorted(list(map(int, input().split())))
result = sum(P)
for i in range(N):
    result += sum(P[:i])
print(result)