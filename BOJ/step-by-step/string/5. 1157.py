# 1157 단어 공부

from collections import Counter
S = Counter(input().upper()).most_common(2)

if len(S) == 1:
    print(S[0][0])
else:
    print('?') if S[0][1] == S[1][1] else print(S[0][0])