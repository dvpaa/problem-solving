# 1541 잃어버린 괄호

S = input() # 55-50+40
arr = S.split('-')
result = sum(map(int, arr[0].split('+')))
for i in range(1, len(arr)):
    result = result - sum(map(int, arr[i].split('+')))
print(result)