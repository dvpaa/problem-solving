import sys

fast_input = sys.stdin.readline

left_stack = list(fast_input().rstrip())
right_stack = []

for _ in range(int(fast_input())):
    operator = fast_input().rstrip().split()
    if operator[0] == "L" and left_stack:
        right_stack.append(left_stack.pop())

    elif operator[0] == "D" and right_stack:
        left_stack.append(right_stack.pop())

    elif operator[0] == "B" and left_stack:
        left_stack.pop()

    elif operator[0] == "P":
        left_stack.append(operator[1])


print("".join(left_stack), end="")
print("".join(right_stack[::-1]))
