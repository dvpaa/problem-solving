# 10828 스택

import sys

stack = []
for _ in range(int(sys.stdin.readline())):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        stack.append(int(com[1]))
    elif com[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif com[0] == 'size':
        print(len(stack))
    elif com[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif com[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)