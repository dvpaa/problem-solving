# 1065 한수

def han(n):
    new = str(n)
    if len(new) == 1:
        return True
    for i in range(len(new)-1):
        d = (int(new[0]) - int(new[-1])) / (len(new) - 1)
        if int(new[i]) - int(new[i+1]) != d:
            return False
    return True

N = int(input())
cnt = 0
for i in range(1, N+1):
    if han(i):
        cnt += 1
print(cnt)