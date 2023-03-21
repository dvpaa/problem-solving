n = int(input())
datas = list(map(int, input().split()))

mapper = {idx: datas[idx] for idx in range(n)}
result = [0] * n
left_stack = [x for x in range(n)]
right_stack = []

while left_stack:
    stand = left_stack.pop()
    
    while right_stack:
        if mapper[stand] > mapper[right_stack[-1]]:
            idx = right_stack.pop()
            result[idx] = stand+1
        else:
            break
    
    right_stack.append(stand)

print(*result)
