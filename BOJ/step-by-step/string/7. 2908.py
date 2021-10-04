# 2908 상수

A, B = input().split()
print(int(A[::-1])) if A[::-1] > B[::-1] else print(int(B[::-1]))