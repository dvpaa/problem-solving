# 15649 N과 M (1)

N, M = map(int, input().split())
result = []


def back_track() -> None:
    if len(result) == M:
        print(*result, sep=' ')
        return

    for i in range(1, N + 1):
        if i not in result:
            result.append(i)
            back_track()
            result.pop()


back_track()
