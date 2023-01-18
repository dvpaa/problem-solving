import math
a, b = map(int, input().split())
table = [False] * (b-a+1)

for i in range(2, int(b ** 0.5) + 1):
    j = int(math.ceil(a / (i ** 2)))
    while True:
        k = i**2 * j
        j += 1
        if k > b:
            break
        table[k-a] = True

print(len([x for x in table if not x]))
