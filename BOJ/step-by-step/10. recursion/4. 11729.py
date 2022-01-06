# 11729 하노이 탑 이동 순서
L = []
def hanoi(n, start, via, end):
    if n == 1:
        L.append([start, end])
    else:
        hanoi(n-1, start, end, via)
        L.append([start, end])
        hanoi(n-1, via, start, end)
n = int(input())
hanoi(n, 1, 2, 3)
print(len(L))
for l in L:
    print(*l, sep=' ')