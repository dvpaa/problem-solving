# Hashing

L = int(input())
S = input()

result = 0
for idx, val in enumerate(S):
    result += (ord(val) - 96) * (31 ** idx)

print(result % 1234567891)