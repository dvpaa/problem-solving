# 문자열 폭발

string = input()
target = input()

last_char = target[-1]
stack = []
length = len(target)

for char in string:
    stack.append(char)
    if char == last_char and ''.join(stack[-length:]) == target:
        for _ in range(length):
            stack.pop()

answer = ''.join(stack)

if not answer:
    print("FRULA")
else:
    print(answer)