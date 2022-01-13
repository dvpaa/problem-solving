# 9375 패션왕 신해빈

for _ in range(int(input())):
    n = int(input())
    clothes = dict()
    for __ in range(n):
        cloth, c_type = input().split()
        if c_type in clothes:
            clothes[c_type] += 1
        else:
            clothes[c_type] = 1
    if len(clothes.keys()) == 1:
        print(list(clothes.values())[0])
    else:
        result = 1
        for i in clothes.values():
            result *= i+1
        print(result - 1)