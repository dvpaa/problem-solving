# 1874 스택 수열

from collections import deque
n = int(input())
data = [int(input()) for _ in range(n)]
arr = deque(data)
s_arr = sorted(arr)
stack = [s_arr[0]]
result = ['+']
a = arr.popleft()

for i in range(1, n):
    while True:
        if stack:
            if stack[-1] == a:
                result.append('-')
                stack.pop()
                if arr:
                    a = arr.popleft()
                    continue
                else:
                    break
            else:
                stack.append(s_arr[i])
                result.append('+')
                break
        else:
            stack.append(s_arr[i])
            result.append('+')
            break
if len(result) + len(stack) == 2*n:
    if stack[::-1] == data[n-len(stack):]:
        result = result + ['-']*len(stack)
        print(*result, sep='\n')
    else:
        print('NO')
else:
    print('NO')