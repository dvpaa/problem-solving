# 2609 최대공약수와 최소공배수

import math

n, m = map(int, input().split())
print(math.gcd(n,m))
print(n * m // math.gcd(n,m))