# N과 M (3)

N, M = map(int, input().split())
result = []


def back_track():
    if len(result) == M:
        print(*result)
        return

    for i in range(1, N + 1):
        result.append(i)
        back_track()
        result.pop()


back_track()
