# DSLR

from collections import deque
import sys

input = sys.stdin.readline


def convert_string(operator: str, val: int) -> int:
    if operator == "D":
        return 2 * val % 10000

    elif operator == "S":
        return 9999 if val == 0 else val-1

    elif operator == "L":
        str_num = "0" * (4 - len(str(val))) + str(val)
        return int(str_num[1] + str_num[2] + str_num[3] + str_num[0])

    elif operator == "R":
        str_num = "0" * (4 - len(str(val))) + str(val)
        return int(str_num[3] + str_num[0] + str_num[1] + str_num[2])


def bfs(init_val: int) -> None:
    queue = deque([init_val])
    while True:
        current_val = queue.popleft()
        for op in std_op:
            new_val = convert_string(op, current_val)
            if not visited[new_val]:
                visited[new_val] = True
                prev[new_val] = (op, current_val)
                if new_val == target_val:
                    return
                queue.append(new_val)


std_op = ["D", "S", "L", "R"]

for _ in range(int(input())):
    init_val, target_val = map(int, input().split())
    visited = [False] * 10000
    prev = [None] * 10000

    bfs(init_val)

    result = []
    while True:
        if prev[target_val] is None or target_val == init_val:
            print("".join(result[::-1]))
            break

        result.append(prev[target_val][0])
        target_val = prev[target_val][1]
