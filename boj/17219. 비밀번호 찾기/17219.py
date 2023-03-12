import sys

input = sys.stdin.readline

N, M = map(int, input().split())
passwords = dict()

for _ in range(N):
    site, password = input().rstrip().split()
    passwords[site] = password

for _ in range(M):
    print(passwords[input().rstrip()])
