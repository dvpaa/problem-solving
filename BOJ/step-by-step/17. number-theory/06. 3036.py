# 3036 링

import math

N = int(input())
R = list(map(int, input().split()))
for i in R[1:]:
    n = math.gcd(R[0],i)
    print(f'{R[0]//n}/{i//n}')