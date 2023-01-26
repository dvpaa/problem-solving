from collections import deque

def solution(priorities, location):
    q = deque([(idx, priority) for idx, priority in enumerate(priorities)])
    cnt = 0
    
    while q:
        idx, priority = q.popleft()
        if is_vaild(q, priority):
            cnt += 1
            if idx == location:
                break
        else:
            q.append((idx, priority))
            
    return cnt

        
def is_vaild(q, target):
    for idx, val in q:
        if val > target:
            return False
    return True
