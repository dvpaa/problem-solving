def solution(prices):
    answer = [0] * len(prices)
    stack = [(0, prices[0])]
    
    for time in range(1, len(prices)):
        while stack:
            if stack[-1][1] > prices[time]:
                prev_time, prev_price = stack.pop()
                answer[prev_time] = time - prev_time
            else:
                break
        stack.append((time, prices[time]))

    top_time, top_price = stack.pop()
    while stack:
        time, price = stack.pop()
        answer[time] = top_time - time
    
    return answer
