# 2867 달팽이는 올라가고 싶다

from math import ceil

A, B, V = map(int, input().split())
print(ceil((V-B) / (A-B)))