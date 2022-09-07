# 2675 문자열 반복

T = int(input())
for _ in range(T):
    n, S = input().split()
    print(''.join(map(lambda x: x * int(n), S)))