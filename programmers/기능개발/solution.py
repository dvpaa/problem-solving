import math

def solution(progresses, speeds):
    answer = []
    day = calculate_day(progresses[0], speeds[0])
    cnt = 0
    for progress, speed in zip(progresses, speeds):
        required_day = calculate_day(progress, speed)

        if day >= required_day:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            day = required_day
            
    answer.append(cnt)
    return answer


def calculate_day(progress, speed):
    return math.ceil((100-progress) / speed)
