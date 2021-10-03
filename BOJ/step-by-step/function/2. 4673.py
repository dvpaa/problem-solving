# 4673 셀프 넘버

def d(n):
    new = n + sum(map(int, str(n)))
    return new

dic = {x : False for x in range(1, 10001)}

for i in range(1, 10001):
    n = d(i)
    if n > 10000:
        continue
    if not dic[n]:
        dic[n] = True
        
for i in range(1, 10001):
    if not dic[i]:
        print(i)