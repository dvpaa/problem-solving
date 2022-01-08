# 2577 숫자의 개수

A = int(input())
B = int(input())
C = int(input())

num = A * B * C
result = [0] * 10

for i in str(num):
    for j in range(10):
        if int(i) == j:
            result[j] += 1
            continue
print(*result, sep='\n')