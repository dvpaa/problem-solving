# 1181 단어 정렬

N = int(input())
words = set()
for _ in range(N):
    words.add(input())
words = list(words)
words.sort(key= lambda x: (len(x), x))
print(*words, sep='\n')