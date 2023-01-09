# 나는야 포켓몬 마스터 이다솜

from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
number_key = {}
name_key = {}

for i in range(1, N+1):
    po_name = input().rstrip()
    name_key[po_name] = i
    number_key[i] = po_name

for _ in range(M):
    key = input().rstrip()
    if key in name_key:
        print(name_key[key])
    else:
        print(number_key[int(key)])
