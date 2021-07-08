# 1110 더하기 사이클

N = int(input())
result = [N//10, N%10]
while True:
    result.append((sum(result[-2:])) % 10)
    if result[0:2] == result[-2:]:
        break
print(len(result)-2)