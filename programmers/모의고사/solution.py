def solution(answers):
    solutions = [[1, 2, 3, 4, 5], 
                 [2, 1, 2, 3, 2, 4, 2, 5], 
                 [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    scores = [get_score(answers, solution) for solution in solutions]
    return get_max_idx_list(scores)
    

def get_score(answers: list, solution: list) -> int:
    size = len(solution)
    score = 0
    idx = 0
    
    for answer in answers:
        if solution[idx] == answer:
            score += 1
        idx = (idx+1) % size
    
    return score


def get_max_idx_list(array: list) -> list:
    max_val = max(array)
    return [idx+1 for idx, val in enumerate(array) if val == max_val]
