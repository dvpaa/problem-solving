# 14888 연산자 끼워넣기

N = int(input())
A = list(map(int, input().split()))
oper = list(map(int, input().split()))
op_dict = {0: '+', 1: '-', 2: '*', 3: '//'}
result_arr = []


def dfs(idx, result):
    if idx == N:
        result_arr.append(result)
        return

    for i in range(4):
        if oper[i] > 0:
            if i == 3 and (result * A[idx] < 0):
                val = -(abs(result) // abs(A[idx]))
            else:
                val = eval(str(result) + op_dict[i] + str(A[idx]))
            oper[i] -= 1
            dfs(idx + 1, val)
            oper[i] += 1


dfs(1, A[0])
print(max(result_arr), min(result_arr), sep='\n')
