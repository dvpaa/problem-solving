# 17298 오큰수

N = int(input())
A = list(map(int, input().split()))
result = [-1] * N
stack = [(0, A[0])]
for i in range(1, N):
    while stack:
        if A[i] > stack[-1][1]:
            idx, n = stack.pop()
            result[idx] = A[i]
        else:
            break
    stack.append((i, A[i]))
print(*result)