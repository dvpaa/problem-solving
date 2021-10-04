# 5622 다이얼

S = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0
for s in S:
    for j in dial:
        if s in j:
            result += dial.index(j) + 3
print(result)