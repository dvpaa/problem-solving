def solution(s):
    stack = []
    for element in s:
        if element == '(':
            stack.append(element)
        else:
            if not stack:
                return False
            stack.pop()
    
    return False if stack else True
