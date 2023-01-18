# 10809 알파벳 찾기

S = input()
dic = {x : -1 for x in range(97, 123)}

for i in range(len(S)):
    if dic[ord(S[i])] == -1:
        dic[ord(S[i])] = i

print(*list(dic.values()))