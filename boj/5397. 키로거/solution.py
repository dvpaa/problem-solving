for _ in range(int(input())):
    input_str = input()
    left_stack = []
    right_stack = []
    
    for s in input_str:
        if s == "<":
            if left_stack:
                right_stack.append(left_stack.pop())
        elif s == ">":
            if right_stack:
                left_stack.append(right_stack.pop())
        elif s == "-":
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(s)

    print("".join(left_stack), end="")
    print("".join(right_stack[::-1]))
