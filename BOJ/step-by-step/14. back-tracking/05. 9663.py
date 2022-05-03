# 9663 N-Queen

N = int(input())
result = [0] * N
cnt = 0


def back_track(x):
    global cnt
    if x == N:
        cnt += 1
        return

    for i in range(N):
        result[x] = i
        if is_queen(x):
            back_track(x + 1)


def is_queen(x):
    for i in range(x):
        if result[x] == result[i] or abs(result[x] - result[i]) == abs(x - i):
            return False
    return True


back_track(0)
print(cnt)
