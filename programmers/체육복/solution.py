def solution(n, lost, reserve):
    students = [-1] + [1] * n + [-1]
    for l in lost:
        students[l] -= 1
    for r in reserve:
        students[r] += 1
    
    cnt = 0
    
    for idx in range(1, n+1):
        if students[idx] == 0:
            prev_idx = idx - 1
            next_idx = idx + 1
            
            if students[prev_idx] == 2:
                students[prev_idx] -= 1
                students[idx] += 1
                
            elif students[next_idx] == 2:
                students[next_idx] -= 1
                students[idx] += 1
            
    return count_answer(students)


def count_answer(students: list) -> int:
    cnt = 0
    for student in students:
        if student >= 1:
            cnt += 1
    return cnt
