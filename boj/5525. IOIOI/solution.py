n = int(input())
m = int(input())
s = input()

i = 1
pattern = 0
cnt = 0

while i < m-1:
    if s[i-1] == "I" and s[i] == "O" and s[i+1] == "I":
        pattern += 1
        i += 1
    else:
        pattern = 0
    
    if pattern == n:
        pattern -= 1
        cnt += 1
    
    i += 1

print(cnt)
