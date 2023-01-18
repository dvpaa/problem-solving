# 3052 나머지

numset = set()

for _ in range(10):
    numset.add(int(input()) % 42)

print(len(numset))