# 8958 OX퀴즈

T = int(input())

for i in range(T):
    result = input()
    score = 0
    cnt = 0
    for s in result:
        if s == 'O':
            cnt += 1
        else:
            score += cnt * (cnt + 1) // 2
            cnt = 0
    score += cnt * (cnt + 1) // 2
    print(score)