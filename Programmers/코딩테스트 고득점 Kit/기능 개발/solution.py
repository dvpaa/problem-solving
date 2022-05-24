def solution(progresses, speeds):
    days = []
    for i in range(len(progresses)):
        day = (100-progresses[i]) / speeds[i]
        day = int(day) if int(day) == day else int(day) +1
        days.append(day)

    i = 1
    cnt = 1
    temp = days[0]
    result = []
    while True:
        if i == len(progresses):
            result.append(cnt)
            break

        if temp >= days[i]:
            cnt += 1
            i += 1

        else:
            result.append(cnt)
            temp = days[i]
            i += 1
            cnt = 1

    return result
