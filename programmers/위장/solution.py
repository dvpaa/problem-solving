def solution(clothes):
    cloth_type = dict()
    for cloth in clothes:
        cloth_type.setdefault(cloth[1], 0)
        cloth_type[cloth[1]] += 1
    
    result = 1
    for num in cloth_type.values():
        result *= (num+1)
    
    return result-1
