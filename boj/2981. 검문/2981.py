# 2981 검문

import math

N = int(input())
nums = sorted([int(input()) for _ in range(N)])
temp = 0
for i in range(N-1):
    temp = math.gcd(temp, nums[i+1] - nums[i])

result = []
for j in range(1, int(temp**0.5)+1):
    if temp % j == 0:
        result.append(j)
        result.append(temp//j)
result = sorted(list(set(result)))
print(*result[1:], sep=' ')