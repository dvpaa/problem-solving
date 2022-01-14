# 9012 괄호

for _ in range(int(input())):
    S = input()
    cnt = 0
    for s in S:
        if s == '(':
            cnt += 1
        elif s == ')':
            cnt -= 1
            if cnt == -1:
                print('NO')
                break
    if cnt == 0:
        print('YES')
    elif cnt > 0:
        print('NO')