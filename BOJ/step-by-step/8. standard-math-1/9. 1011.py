# 1011 Fly me to the Alpha Centauri

import math

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    dist = y - x
    root = math.sqrt(dist)
    m = round(root)
    print(2*m - 1) if root <= m else print(2*m)