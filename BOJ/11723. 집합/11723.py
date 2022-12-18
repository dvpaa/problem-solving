# 11723 집합

import sys

input = sys.stdin.readline
S = set()

for _ in range(int(input())):
    operation = input().rstrip().split(" ")

    if operation[0] == "add":
        S.add(int(operation[1]))
    elif operation[0] == "remove":
        if int(operation[1]) in S:
            S.remove(int(operation[1]))
    elif operation[0] == "check":
        print(1) if int(operation[1]) in S else print(0)
    elif operation[0] == "toggle":
        if int(operation[1]) in S:
            S.remove(int(operation[1]))
        else:
            S.add(int(operation[1]))
    elif operation[0] == "all":
        S = {x for x in range(1, 21)}
    elif operation[0] == "empty":
        S = set()
