# 2292 벌집

import math

N = int(input())
print(1) if N == 1 else print(math.ceil((3+math.sqrt(12*N-3))/6))