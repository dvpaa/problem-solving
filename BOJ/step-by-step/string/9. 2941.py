# 2941 크로아티아 알파벳

S = input()
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for al in alpha:
    if al in S:
        cnt += S.count(al)
        S = ','.join(S.split(al))
print(cnt + len(S) - S.count(','))