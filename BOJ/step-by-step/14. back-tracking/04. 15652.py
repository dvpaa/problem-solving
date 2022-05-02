# N과 M (4)

N, M = map(int, input().split())
result = []


def back_track():
    if len(result) == M:
        print(*result)
        return

    for i in range(1, N + 1):
        if is_sorted(result, i):
            result.append(i)
            back_track()
            result.pop()


def is_sorted(arr: list, val: int):
    if len(arr) == 0:
        return True
    if arr[-1] <= val:
        return True
    return False


back_track()
