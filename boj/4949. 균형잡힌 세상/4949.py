# 4949 균형잡힌 세상

while True:
    S = input()
    stack = []
    result = True
    if S == '.':
        break
    for s in S:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack:
                n = stack.pop()
            else:
                result = False
                break
            if n != '(':
                result = False
                break
        elif s == ']':
            if stack:
                n = stack.pop()
            else:
                result = False
                break
            if n != '[':
                result = False
                break
        else:
            continue
    if not result:
        print('no')
    else:
        if stack:
            print('no')
        else:
            print('yes')