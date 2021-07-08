# 10871 X보다 작은 수

N, X = map(int, input().split())
A = list(map(int, input().split()))
print(*[n for n in A if n < X])