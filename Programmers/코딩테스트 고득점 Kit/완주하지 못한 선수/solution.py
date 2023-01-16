def solution(participant, completion):
    people_dict = dict()
    for person in participant:
        people_dict.setdefault(person, 0)
        people_dict[person] += 1
    
    for person in completion:
        people_dict[person] -= 1
    
    for key, val in people_dict.items():
        if val != 0:
            return key
